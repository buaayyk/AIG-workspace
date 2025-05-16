#!/bin/bash

cur_dir=`pwd`
Younger_DiGress_dir=/root/autodl-tmp/AIG/Younger-DiGress

for graph_limit in "300"
do
    cd ${cur_dir}
    
    python scripts/DiGress/format_transform.py ${graph_limit}
    
    cd ${Younger_DiGress_dir}

    CUDA_VISIBLE_DEVICES=0 python main.py \
    --config-dir=${cur_dir}/configs/DiGress \
    --config-name=config \
    dataset=Younger-100 \
    general=general_default \
    model=discrete \
    train=train_default \
    train.batch_size=4 \
    general.final_model_samples_to_generate=32 \
    hydra.run.dir=${cur_dir}/outputs/Younger-${graph_limit}-copy
done