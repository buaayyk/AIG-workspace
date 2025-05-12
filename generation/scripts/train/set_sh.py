for split_method in ["Random", "RandomFull", "Cascade", "CascadeFull", "Window", "MixBasic", "MixSuper", "Full"]:
    for mask_method in ["Random", "Purpose"]:
        s_sh = f'''#!/bin/bash

CUBLAS_WORKSPACE_CONFIG=:4096:8 younger-apps-dl launch \\
    --task-kind ir \\
    --task-name basic_embedding \\
    --task-step train \\
    --toml-path configs/train/MAEGIN_{split_method}_{mask_method}.toml
'''
        with open(f"scripts/train/MAEGIN_{split_method}_{mask_method}.sh", "w") as f:
            f.write(s_sh)