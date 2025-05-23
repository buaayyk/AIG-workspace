#!/bin/bash

export CUDA_VISIBLE_DEVICES=1

methods=("Full" "CascadeFull" "Cascade" "RandomFull")

for method in ${methods[*]}
do
    sh scripts/train/MAEGIN_${method}_Purpose.sh
done