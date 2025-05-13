#!/bin/bash

export CUDA_VISIBLE_DEVICES=1

for split_method in "Cascade" "CascadeFull"  
do
    for mask_method in "Purpose" "Random"
    do
        if [ "${split_method}" = "Cascade" ] && [ "${mask_method}" = "Purpose" ]; then
            continue
        fi
        echo ${split_method}
        echo ${mask_method}
        sh scripts/train/MAEGIN_${split_method}_${mask_method}.sh    
    done
done
