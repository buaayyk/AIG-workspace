#!/bin/bash

export CUDA_VISIBLE_DEVICES=2

for split_method in "Window" "Full"  
do
    for mask_method in "Purpose" "Random"
    do
        if [ "${split_method}" = "Window" ] && [ "${mask_method}" = "Purpose" ]; then
            continue
        fi
        if [ "${split_method}" = "Window" ] && [ "${mask_method}" = "Random" ]; then
            continue
        fi
        echo ${split_method}
        echo ${mask_method}
        sh scripts/train/MAEGIN_${split_method}_${mask_method}.sh    
    done
done
