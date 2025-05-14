
for number_of_levels in [0, 1, 2, 3, 4, 5]:
    for generation_steps in [1, 2, 3, 4, 5, 6]:

        s_sh = f'''#!/bin/bash

CUBLAS_WORKSPACE_CONFIG=:4096:8 younger-apps-dl launch \\
    --task-kind ir \\
    --task-name basic_embedding \\
    --task-step evaluate \\
    --toml-path configs/evaluate_S/MAEGIN_MixSuper_Purpose_S{number_of_levels}_on_G{generation_steps}.toml

'''
        with open(f"scripts/evaluate_S/MAEGIN_MixSuper_Purpose_S{number_of_levels}_on_G{generation_steps}.sh", "w") as f:
            f.write(s_sh)