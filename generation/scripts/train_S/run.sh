#!/bin/bash

export CUDA_VISIBLE_DEVICES=0

for number_of_levels in "1" "2" "3" "4" "5"
do
    sh scripts/train_S/MAEGIN_MixSuper_Purpose_S${number_of_levels}.sh
done
