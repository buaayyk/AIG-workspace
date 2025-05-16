import networkx as nx
import json
import pathlib
from younger_logics_ir.modules import LogicX
import os
import sys

def parse_graph_file(graph_filepath, decoder):
    graphs = []
    with open(graph_filepath, 'r') as f:
        while True:
            line = f.readline().strip()
            if not line:
                break

            if not line.startswith("N="):
                continue

            N = int(line.split('=')[1])

            f.readline()

            node_labels_line = f.readline().strip()
            node_labels = list(map(lambda x: decoder[int(x)] ,node_labels_line.split()))
            if len(node_labels) != N:
                raise ValueError(f"Expected {N} node labels, but found {len(node_labels)} in line: {node_labels_line}")

            f.readline()

            adj_matrix = []
            for _ in range(N):
                row = list(map(int, f.readline().strip().split()))
                if len(row) != N:
                    raise ValueError(f"Expected {N} values in adjacency matrix row, but found {len(row)}: {row}")
                adj_matrix.append(row)

            graph = nx.DiGraph()
            for i in range(N):
                graph.add_node(i, uuid=node_labels[i])
            for i in range(N):
                for j in range(i + 1, N):
                    if adj_matrix[i][j] == 1:
                        graph.add_edge(i, j)

            graphs.append(graph)

            f.readline()

    return graphs


if __name__ == '__main__':
    chunk_idx = int(sys.argv[1])
    graph_filepath = f"outputs/Younger-200/generated_samples{chunk_idx}.txt"
    codebook_filepath = "data/DiGress_data/codebook.json" 
    save_dirpath = pathlib.Path("generated_graphs/DiGress")
    with open(codebook_filepath, "r") as f:
        codebook = json.load(f)
    decoder = {v:k for k, v in codebook.items()}

    graphs = parse_graph_file(graph_filepath, decoder)

    idx = len(os.listdir(save_dirpath))
    for dag in graphs:
        logicx = LogicX()
        logicx.setup_dag(dag)
        logicx.save(save_dirpath / str(idx))
        idx += 1

