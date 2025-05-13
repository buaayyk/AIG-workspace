for number_of_levels in [1, 2, 3, 4, 5]:

    s_sh = f'''#!/bin/bash

CUBLAS_WORKSPACE_CONFIG=:4096:8 younger-apps-dl launch \\
    --task-kind ir \\
    --task-name basic_embedding \\
    --task-step train \\
    --toml-path configs/train_S/MAEGIN_MixSuper_Purpose_S{number_of_levels}.toml

'''
    with open(f"scripts/train_S/MAEGIN_MixSuper_Purpose_S{number_of_levels}.sh", "w") as f:
        f.write(s_sh)