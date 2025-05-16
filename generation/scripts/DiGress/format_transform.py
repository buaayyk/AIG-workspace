import pathlib
from younger_logics_ir.modules import LogicX
from younger.commons.io import load_json, save_json
import os
import tqdm
import torch
import sys

graph_limit = int(sys.argv[1])

load_dirpath = "data/Full"
meta_filepath = f"{load_dirpath}/training/meta.json"
save_dirpath = "data/DiGress_data"

meta = load_json(meta_filepath)
node_types = ['__UNK__'] + ['__MASK__'] + meta['node_types']
codebook = {}
for i, node_type in enumerate(node_types):
    codebook[node_type] = i

logicx_filepaths = []
for split in ["training", "validation", "test"]:
    split_dirpath = f"{load_dirpath}/{split}/items"
    for filename in os.listdir(split_dirpath):
        logicx_filepaths.append(f"{split_dirpath}/{filename}")

data = []

for logicx_filepath in tqdm.tqdm(logicx_filepaths):
    logicx = LogicX()
    logicx.load(pathlib.Path(logicx_filepath))

    X = []
    node2idx = dict()
    for i, node in enumerate(logicx.dag.nodes()):
        node_type = logicx.dag.nodes[node]['node_uuid']
        X.append(codebook[node_type])
        node2idx[node] = i

    src = []
    dst = []
    for u, v in logicx.dag.edges():
        src.append(node2idx[u])
        dst.append(node2idx[v])
    edge_index = [src, dst]

    datapoint = {
        "X": X,
        "edge_index": edge_index
    }

    if len(X) > graph_limit:
        continue
    data.append(datapoint)

torch.save(data, f"{save_dirpath}/Younger-{graph_limit}.zip")
save_json(codebook, f"{save_dirpath}/codebook.json", indent=2)
with open(f"{save_dirpath}/Younger-{graph_limit}-{len(data)}.txt", "w") as f:
    f.write("")