#!/bin/bash

export CUDA_VISIBLE_DEVICES=1
MODEL_PATH="/home/lan/CodeSpace/FastChat/output/vicuna7b_alpaca52k_1/checkpoint-"
MODEL_NOS=("318" "636" "954" "1272" "1590")

for MODEL_NO in "${MODEL_NOS[@]}"
do
    # 构建完整的模型路径
    FULL_MODEL_PATH="${MODEL_PATH}${MODEL_NO}"

    # 在这里执行你想要的操作，使用 $FULL_MODEL_PATH 来访问当前迭代的模型路径
    echo "Processing model: $FULL_MODEL_PATH"
    MODEL_ID="vicuna_7b_alpaca52k_1_ckpt${MODEL_NO}"
    echo "Processing model id: $MODEL_ID"
    # 例如，可以调用 Python 脚本，并将模型路径作为参数传递
    python /home/lan/CodeSpace/FastChat/get_model_answer.py --model-id $MODEL_ID --model-path $FULL_MODEL_PATH --question-file /home/lan/CodeSpace/FastChat/fastchat/eval/table/question.jsonl --answer-file "/home/lan/CodeSpace/FastChat/fastchat/eval/table/answer/answer_${MODEL_ID}.jsonl" --num-gpus 1

    # 或者可以执行其他操作，如复制、移动或删除文件等
done


# MODEL_PATH=/home/lan/CodeSpace/FastChat/output/vicuna_7b_alpaca1/checkpoint-298
# MODEL_ID=vicuna_7b_alpaca1_ckpt298