#!/usr/bin
num_gpus=1
gpu="3"
max_gpu_memory="24Gib"
checkpoint=$((298 * 2))
model_path="/home/lan/CodeSpace/FastChat/output/vicuna_7b_alpaca1/checkpoint-$checkpoint"
python3 -m fastchat.serve.cli --model-path "$model_path" --gpus "$gpu" --max-gpu-memory "$max_gpu_memory" 