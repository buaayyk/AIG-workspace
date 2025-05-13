#!/bin/bash

export CUDA_VISIBLE_DEVICES=0
methods=("Window" "MixBasic" "MixSuper" "Random")

for method in ${methods[*]}
do
    sh scripts/train/MAEGIN_${method}_Random.sh
done
