#!/bin/bash

export CUDA_VISIBLE_DEVICES=2
methods=("Window" "MixBasic" "MixSuper")

for method in ${methods[*]}
do
    sh scripts/preprocess/${method}.sh
done

# for method in ${methods[*]}
# do
#     sh scripts/train/MAEGIN_${method}_Random.sh
# done

# for method in ${methods[*]}
# do
#     sh scripts/train/MAEGIN_${method}_Purpose.sh
# done