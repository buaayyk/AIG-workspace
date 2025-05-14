#!/bin/bash

CUBLAS_WORKSPACE_CONFIG=:4096:8 younger-apps-dl launch \
    --task-kind ir \
    --task-name basic_embedding \
    --task-step evaluate \
    --toml-path configs/evaluate/MAEGIN_CascadeFull_Random_on_MixSuper_Random.toml

