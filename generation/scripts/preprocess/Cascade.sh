#!/bin/bash

younger-apps-dl launch \
    --task-kind ir \
    --task-name basic_embedding \
    --task-step preprocess \
    --toml-path configs/preprocess/Cascade.toml
