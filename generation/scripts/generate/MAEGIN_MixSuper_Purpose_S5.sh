#!/bin/bash

CUBLAS_WORKSPACE_CONFIG=:4096:8 younger-apps-dl launch \
    --task-kind ir \
    --task-name basic_embedding \
    --task-step predict \
    --toml-path configs/generate/MAEGIN_MixSuper_Purpose_S5.toml