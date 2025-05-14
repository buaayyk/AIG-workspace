#!/bin/bash

CUBLAS_WORKSPACE_CONFIG=:4096:8 younger-apps-dl launch \
    --task-kind ir \
    --task-name basic_embedding \
    --task-step evaluate \
    --toml-path configs/evaluate_S/MAEGIN_MixSuper_Purpose_S2_on_G4.toml

