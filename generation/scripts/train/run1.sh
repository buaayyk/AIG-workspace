#!/bin/bash

export CUDA_VISIBLE_DEVICES=0

for split_method in "Random" "RandomFull"  
do

    for mask_method in "Purpose" "Random"
    do
        if [ "${split_method}" = "Random" ] && [ "${mask_method}" = "Purpose" ]; then
            continue
        fi
        echo ${split_method}
        echo ${mask_method}
        sh scripts/train/MAEGIN_${split_method}_${mask_method}.sh    
    done
done
