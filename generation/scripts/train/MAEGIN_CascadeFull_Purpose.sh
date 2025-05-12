#!/bin/bash

CUBLAS_WORKSPACE_CONFIG=:4096:8 younger-apps-dl launch \
    --task-kind ir \
    --task-name basic_embedding \
    --task-step train \
    --toml-path configs/train/MAEGIN_CascadeFull_Purpose.toml
