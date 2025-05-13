#!/bin/bash

for split_method in "CascadeFull" "RandomFull"
do
    sh scripts/preprocess/${split_method}.sh
done

export CUDA_VISIBLE_DEVICES=2
methods=("RandomFull" "Cascade" "CascadeFull" "Full")

for method in ${methods[*]}
do
    sh scripts/train/MAEGIN_${method}_Random.sh
done
