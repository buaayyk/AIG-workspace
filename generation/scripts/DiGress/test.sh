cur_dir=`pwd`
Younger_DiGress_dir=/root/autodl-tmp/AIG/Younger-DiGress

graph_limit=200

cd ${Younger_DiGress_dir}

for i in "2" "3" "4" "5" "6" "7" "8" "9" "10" "11" "12"
do
    CUDA_VISIBLE_DEVICES=0 python main.py \
        --config-dir=${cur_dir}/configs/DiGress \
        --config-name=config \
        dataset=Younger-${graph_limit} \
        general=general_default \
        model=discrete \
        train=train_default \
        train.batch_size=4 \
        general.test_only=True \
        general.final_model_samples_to_generate=128 \
        hydra.run.dir=${cur_dir}/outputs/Younger-${graph_limit}
done

# OUTPUT_DIR=/home2/yyk/diffusion/NSG/outputs/2025-04-25/13-24-30
# CUDA_VISIBLE_DEVICES=3 python main.py \
#     dataset=nasbench201_cifar10 \
#     model=discrete \
#     general=general_default \
#     train=train_default \
#     general.test_only=True \
#     general.final_model_samples_to_generate=1920 \
#     general.resume=${OUTPUT_DIR}/checkpoints/graph-tf-model \
#     hydra.run.dir=${OUTPUT_DIR}