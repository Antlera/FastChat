import torch

# 指定模型文件的路径
model_path = "/home/lan/CodeSpace/FastChat/output/vicuna_7b_dummy11/pytorch_model-00001-of-00002.bin"

# 加载模型
model = torch.load(model_path)
new_model_path = "/home/lan/CodeSpace/FastChat/output/vicuna_7b_dummy11_resave/pytorch_model-00001-of-00002.bin"

# 保存模型
torch.save(model, new_model_path)