import ast
import onnx
import os
import pathlib
import tqdm

from younger.commons.io import create_dir, load_json
from younger_logics_ir.modules import LogicX


def _check_valid_(uuid2tuid_mapping_filepath, node_uuids: str, in_degrees: int, out_degrees: int) -> float:
    uuid2tuid = load_json(uuid2tuid_mapping_filepath) 
    total_nodes = len(node_uuids)
    valid_node_count = 0
    cannot_valid_node_count = 0
    for node_uuid, in_degree, out_degree in zip(node_uuids, in_degrees, out_degrees):
        check_flag = False
        try:
            op_type = ast.literal_eval(uuid2tuid[node_uuid][len('operator-'):])[0]
            domain = ast.literal_eval(uuid2tuid[node_uuid][len('operator-'):])[1]
            schema = onnx.defs.get_schema(op_type, domain=domain)
        except Exception as e:
            cannot_valid_node_count += 1
            continue
        if len(schema.inputs) > 0:
            last_input = schema.inputs[-1]
            if last_input.option.value == last_input.option.Optional.value:
                if in_degree <= len(schema.inputs):
                    check_flag = True
            if last_input.option.value == last_input.option.Variadic.value:
                if in_degree >= len(schema.inputs) - 1:
                    check_flag = True
            else:
                if in_degree == len(schema.inputs):
                    check_flag = True
        if len(schema.outputs) > 0:
            last_output = schema.outputs[-1]
            if last_output.option.value == last_output.option.Optional.value:
                if out_degree <= len(schema.outputs):
                    check_flag = True
            if last_output.option.value == last_output.option.Variadic.value:
                if out_degree >= len(schema.outputs) - 1:
                    check_flag = True
            else:
                if out_degree == len(schema.outputs):
                    check_flag = True
        if check_flag:
            valid_node_count += 1
    valid_nodes_ratio = valid_node_count / total_nodes
    failed2check_valid_nodes_ratio = cannot_valid_node_count / total_nodes
    return valid_nodes_ratio, failed2check_valid_nodes_ratio 


if __name__ == "__main__":
    name = "DiGress"
    for name in ["DiGress", "step-by-step", "step-by-step-S5"]:
        load_dirpath = pathlib.Path(f"generated_graphs/{name}")
        uuid2tuid_mapping_filepath = pathlib.Path("configs/generate/uuid2tuid.json")

        node_uuids = []
        in_degrees = []
        out_degrees = []
        for filepath in tqdm.tqdm(list(os.listdir(load_dirpath))):
            filepath = load_dirpath / filepath
            logicx = LogicX()
            logicx.load(filepath)
            for node in logicx.dag.nodes():
                uuid = logicx.dag.nodes[node]['uuid']
                in_degree = logicx.dag.in_degree(node)
                out_degree = logicx.dag.out_degree(node)
                node_uuids.append(uuid)
                in_degrees.append(in_degree)
                out_degrees.append(out_degree)
        # print(node_uuids)
        # print(in_degrees)
        # print(out_degrees)
        print(name)
        print(_check_valid_(uuid2tuid_mapping_filepath, node_uuids, in_degrees, out_degrees))
    

    # idx = len(os.listdir(save_dirpath))
    # for dag in graphs:
    #     logicx = LogicX()
    #     logicx.setup_dag(dag)
    #     logicx.save(save_dirpath / str(idx))
    #     idx += 1
    # pass