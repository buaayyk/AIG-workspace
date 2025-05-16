#!/bin/bash

cur_dir=`pwd`
Younger_DiGress_dir=/root/autodl-tmp/AIG/Younger-DiGress

# for graph_limit in "400" "500" "600" "700" "800"

# for graph_limit in "1000" "900" "800" "700" "600" "500" "400"
# for graph_limit in "100"
for graph_limit in "200"
do
    # cd ${cur_dir}
    
    # python scripts/DiGress/format_transform.py ${graph_limit}
    
    cd ${Younger_DiGress_dir}

    CUDA_VISIBLE_DEVICES=0 python main.py \
    --config-dir=${cur_dir}/configs/DiGress \
    --config-name=config \
    dataset=Younger-${graph_limit} \
    general=general_default \
    model=discrete \
    train=train_default \
    train.batch_size=4 \
    general.final_model_samples_to_generate=32 \
    hydra.run.dir=${cur_dir}/outputs/Younger-${graph_limit}
done