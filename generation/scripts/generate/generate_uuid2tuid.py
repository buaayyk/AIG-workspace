import ast
import click
import pathlib
import multiprocessing

from tqdm import tqdm
from typing import Any
from younger_logics_ir.modules import LogicX
from younger.commons.io import save_json

uuid2tuid = dict()

def traverse_pipeline(skeleton_filepath: pathlib.Path) -> tuple[str, dict[str, str], bool]:
    local_map = {}
    logicx = LogicX()
    logicx.load(skeleton_filepath)
    flag = True
    for node_index in logicx.dag.nodes():
        node_uuid = logicx.dag.nodes[node_index]['node_uuid']
        node_tuid = logicx.node_tuid_feature(node_index)
        node_type = logicx.node_type_feature(node_index)
        if node_type != "operator":
            continue
        op_type = ast.literal_eval(node_tuid[len('operator-'):])[0]
        if node_uuid not in local_map:
            local_map[node_uuid] = node_tuid
        else:
            if local_map[node_uuid] != node_tuid:
                flag = False
    return skeleton_filepath, local_map, flag

@click.command()
@click.option('--skeleton-filepath', type=click.Path(exists=True, file_okay=False, path_type=pathlib.Path), default=None, help='Path to the skeleton directory.')
@click.option('--save-dir', type=click.Path(file_okay=False, path_type=pathlib.Path), default=None, help='Path to save output files.')
@click.option('--num-workers', type=int, default=12, help='Number of workers to use.')
def main(skeleton_filepath, save_dir, num_workers):
    uuid2tuid = {}
    skeleton_filepaths = list(skeleton_filepath.iterdir())
    success = 0
    failed = 0
    with multiprocessing.Pool(num_workers) as pool:
        with tqdm(total=len(skeleton_filepaths), desc='Traversing') as progress_bar:
            for skeleton_file_path, local_map, flag in pool.imap(traverse_pipeline, skeleton_filepaths):
                for uuid, tuid in local_map.items():
                    if uuid not in uuid2tuid:
                        uuid2tuid[uuid] = tuid
                        success += 1
                    elif uuid2tuid[uuid] != tuid or not flag:
                        failed += 1
                progress_bar.set_description(f'processing - {skeleton_file_path.stem} - success {success} - failed {failed}') 
                progress_bar.update(1)
    
    save_json(uuid2tuid, save_dir.joinpath("uuid2tuid.json"), indent=2)


if __name__ == "__main__":
    main()