"""Generate json file for webpage."""
import json
import os
import re

models = ["ckpt298", "vicuna"]

# 获取当前工作目录
current_directory = os.getcwd()

# 打印当前工作目录
print("Current directory:", current_directory)
def read_jsonl(path: str, key: str = None):
    data = []
    with open(os.path.expanduser(path)) as f:
        for line in f:
            if not line:
                continue
            data.append(json.loads(line))
    if key is not None:
        data.sort(key=lambda x: x[key])
        data = {item[key]: item for item in data}
    return data


def trim_hanging_lines(s: str, n: int) -> str:
    s = s.strip()
    for _ in range(n):
        s = s.split("\n", 1)[1].strip()
    return s


if __name__ == "__main__":
    questions = read_jsonl("table/question.jsonl", key="question_id")

    ckpt298_answers = read_jsonl("/home/lan/CodeSpace/FastChat/fastchat/eval/table/answer/answer_vicuna_7b_alpaca1_ckpt298.jsonl", key="question_id")
    ckpt596_answers = read_jsonl("/home/lan/CodeSpace/FastChat/fastchat/eval/table/answer/answer_vicuna_7b_alpaca1_ckpt596.jsonl", key="question_id")


    review_ckpt298 = read_jsonl(
        "/home/lan/CodeSpace/FastChat/fastchat/eval/table/review/vicuna_7b_alpaca1/review_ckpt298_ckpt1192.jsonl"
    )

    records = []
    for qid in questions.keys():
        r = {
            "id": qid,
            "category": questions[qid]["category"],
            "question": questions[qid]["text"],
            "answers": {
                "ckpt298": ckpt298_answers[qid]["text"],
                "vicuna": ckpt596_answers[qid]["text"],
            },
            "evaluations": {
                "ckpt298": review_ckpt298[qid]["text"],
            },
            "scores": {
                "ckpt298": review_ckpt298[qid]["score"],
            },
        }

        # cleanup data
        cleaned_evals = {}
        for k, v in r["evaluations"].items():
            v = v.strip()
            lines = v.split("\n")
            # trim the first line if it's a pair of numbers
            if re.match(r"\d+[, ]+\d+", lines[0]):
                lines = lines[1:]
            v = "\n".join(lines)
            cleaned_evals[k] = v.replace("Assistant 1", "**Assistant 1**").replace(
                "Assistant 2", "**Assistant 2**"
            )

        r["evaluations"] = cleaned_evals
        records.append(r)

    # Reorder the records, this is optional
    for r in records:
        if r["id"] <= 20:
            r["id"] += 60
        else:
            r["id"] -= 20
    for r in records:
        if r["id"] <= 50:
            r["id"] += 10
        elif 50 < r["id"] <= 60:
            r["id"] -= 50
    for r in records:
        if r["id"] == 7:
            r["id"] = 1
        elif r["id"] < 7:
            r["id"] += 1

    records.sort(key=lambda x: x["id"])

    # Write to file
    with open("webpage/data.json", "w") as f:
        json.dump({"questions": records, "models": models}, f, indent=2)
