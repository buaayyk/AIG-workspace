#!/bin/bash

export CUDA_VISIBLE_DEVICES=1

for task in "MAEGIN_Cascade_Purpose" "MAEGIN_Random_Purpose"
do
    sh scripts/train/${task}.sh
done