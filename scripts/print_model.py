import torch

# 指定模型文件的路径
model_path = "/home/lan/CodeSpace/FastChat/output/vicuna_7b_dummy11/pytorch_model-00001-of-00002.bin"

# 加载模型
model = torch.load(model_path)

# 打印模型
print(model)

# 打印模型的键和对应的值
for k in model.keys():
    print(f"Key: {k}")
    if isinstance(model[k], torch.Tensor):
        # 如果值是张量，则打印张量的形状和数据类型
        print(f"Shape: {model[k].shape}")
        print(f"Data Type: {model[k].dtype}")
    else:
        # 否则，直接打印值
        print(f"Value: {model[k]}")
