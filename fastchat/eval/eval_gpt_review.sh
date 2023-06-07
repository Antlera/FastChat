MODEL_NOS=("298" "596" "894")

for MODEL_NO in "${MODEL_NOS[@]}"
do
    # 例如，可以调用 Python 脚本，并将模型路径作为参数传递
    python eval_gpt_review.py -q table/question.jsonl -a /home/lan/CodeSpace/FastChat/fastchat/eval/table/answer/answer_vicuna_7b_alpaca1_ckpt${MODEL_NO}.jsonl /home/lan/CodeSpace/FastChat/fastchat/eval/table/answer/answer_vicuna_7b_alpaca1_ckpt1192.jsonl -p table/prompt.jsonl -r table/reviewer.jsonl -o /home/lan/CodeSpace/FastChat/fastchat/eval/table/review/vicuna_7b_alpaca1/review_ckpt${MODEL_NO}_ckpt1192.jsonl
    # 或者可以执行其他操作，如复制、移动或删除文件等
done

