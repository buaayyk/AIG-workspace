for split_method in ["Random", "RandomFull", "Cascade", "CascadeFull", "Window", "MixBasic", "MixSuper", "Full"]:

    s_sh = f'''#!/bin/bash

younger-apps-dl launch \\
    --task-kind ir \\
    --task-name basic_embedding \\
    --task-step preprocess \\
    --toml-path configs/preprocess/{split_method}.toml
'''
    with open(f"scripts/preprocess/{split_method}.sh", "w") as f:
        f.write(s_sh)