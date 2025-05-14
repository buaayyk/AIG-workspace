#!/bin/bash

export CUDA_VISIBLE_DEVICES=1

for number_of_levels in "0" "1" "2" "3" "4" "5"
do
    for generation_steps in "1" "2" "3" "4" "5" "6"
    do
        sh scripts/evaluate_S/MAEGIN_MixSuper_Purpose_S${number_of_levels}_on_G${generation_steps}.sh
    done
done
