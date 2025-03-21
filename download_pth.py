import sys
import requests
import os
import sysconfig
import torch
from tqdm import tqdm  # 导入 tqdm 库

if __name__ == "__main__":
    if torch.cuda.is_available():
        url = "https://www.iplant.cn/dsite/apt/download.php?tf=12"
        file_name = "sam_vit_h_4b8939.pth"
    else:
        url = "https://www.iplant.cn/dsite/apt/download.php?tf=11"
        file_name = "sam_vit_b_01ec64.pth"
    
    base_dir = sysconfig.get_paths()["purelib"]
    dest_dir = os.path.join(base_dir, "ElliShape")
    os.makedirs(dest_dir, exist_ok=True)
    file_path = os.path.join(dest_dir, file_name)
    
    # 下载文件
    try:
        print(f"Downloading {file_name} from {url} to {dest_dir}...")
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # 获取文件总大小（以字节为单位）
        total_size = int(response.headers.get("content-length", 0))
        
        # 使用 tqdm 创建进度条
        with open(file_path, "wb") as f:
            with tqdm(total=total_size, unit="B", unit_scale=True, desc=file_name) as pbar:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        pbar.update(len(chunk))  # 更新进度条
        
        print(f"Download complete! File saved to: {file_path}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {file_name}: {e}")