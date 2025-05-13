#!/bin/bash

export CUDA_VISIBLE_DEVICES=3

methods=("Random" "MixSuper" "MixBasic" "Window")

for method in ${methods[*]}
do
    sh scripts/train/MAEGIN_${method}_Purpose.sh
done