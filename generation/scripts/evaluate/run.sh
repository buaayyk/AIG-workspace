#!/bin/bash

export CUDA_VISIBLE_DEVICES=1

for mask_method in "Random" "Purpose"
do
    for split_method_train in "Random" "RandomFull" "Cascade" "CascadeFull" "Window" "MixBasic" "MixSuper" "Full"
    do
        for split_method_test in "Random" "RandomFull" "Cascade" "CascadeFull" "Window" "MixBasic" "MixSuper" "Full"
        do
            sh scripts/evaluate/MAEGIN_${split_method_train}_${mask_method}_on_${split_method_test}_${mask_method}.sh
        done
    done        
done
    