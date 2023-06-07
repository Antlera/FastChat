#!/bin/bash
export CUDA_VISIBLE_DEVICES=3
MODEL_PATH="/home/lan/CodeSpace/FastChat/output/vicuna7b_alpaca52k_1/checkpoint-"
MODEL_NOS=("318" "636" "954" "1272" "1590")

for MODEL_NO in "${MODEL_NOS[@]}"
do
    # 构建完整的模型路径
    FULL_MODEL_PATH="${MODEL_PATH}${MODEL_NO}"

    # 在这里执行你想要的操作，使用 $FULL_MODEL_PATH 来访问当前迭代的模型路径
    echo "Processing model: $FULL_MODEL_PATH"
    checkpoint_dir="$FULL_MODEL_PATH"
    output_file="$checkpoint_dir/pytorch_model.bin"
    # 例如，可以调用 Python 脚本，并将模型路径作为参数传递
    python /home/lan/CodeSpace/FastChat/scripts/zero_to_fp32.py "$checkpoint_dir" "$output_file"
    # 或者可以执行其他操作，如复制、移动或删除文件等
done





