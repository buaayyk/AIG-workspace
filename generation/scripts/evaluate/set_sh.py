for mask_method in ["Random", "Purpose"]:
    for split_method_train in ["Random", "RandomFull", "Cascade", "CascadeFull", "Window", "MixBasic", "MixSuper", "Full"]:
        for split_method_test in ["Random", "RandomFull", "Cascade", "CascadeFull", "Window", "MixBasic", "MixSuper", "Full"]:

            s_sh = f'''#!/bin/bash

CUBLAS_WORKSPACE_CONFIG=:4096:8 younger-apps-dl launch \\
    --task-kind ir \\
    --task-name basic_embedding \\
    --task-step evaluate \\
    --toml-path configs/evaluate/MAEGIN_{split_method_train}_{mask_method}_on_{split_method_test}_{mask_method}.toml

'''
            with open(f"scripts/evaluate/MAEGIN_{split_method_train}_{mask_method}_on_{split_method_test}_{mask_method}.sh", "w") as f:
                f.write(s_sh)