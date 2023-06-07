import json

# 读取 JSON 文件
with open('/home/lan/CodeSpace/FastChat/playground/data/CrimeKgAssitantClean_52k.json', 'r', encoding='UTF-8') as f:
    input_data = json.load(f)

output_data = []

# 处理输入数据并生成输出数据
for idx, data in enumerate(input_data):
    output_data.append({
        "id": f"identity_{idx}",
        "conversations": [
            {
                "from": "human",
                "value": f"{data['input']}"
            },
            {
                "from": "gpt",
                "value": data['output']
            }
        ]
    })

# 打印输出数据
# for data in output_data:
#     print(data)
# 将输出数据保存到 JSON 文件
with open('/home/lan/CodeSpace/FastChat/playground/data/CrimeKgAssitantClean_52k_vicuna.json', 'w', encoding='UTF-8') as f:
    json.dump(output_data, f, indent=4, ensure_ascii=False)
