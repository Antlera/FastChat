import torch

def print_gpu_info():
    if torch.cuda.is_available():
        num_gpus = torch.cuda.device_count()
        print(f"Number of available GPUs: {num_gpus}")
        for i in range(num_gpus):
            gpu_info = torch.cuda.get_device_properties(i)
            print(f"\n=== GPU {i} ===")
            print(f"Name: {gpu_info.name}")
            print(f"Total Memory: {gpu_info.total_memory / (1024**3):.2f} GB")
            print(f"Multi-Processor Count: {gpu_info.multi_processor_count}")
            print(f"CUDA Capability: {gpu_info.major}.{gpu_info.minor}")
    else:
        print("No GPUs available.")

# 调用函数打印GPU信息
print_gpu_info()
