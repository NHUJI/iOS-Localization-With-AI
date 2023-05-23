import os
import shutil

# 这是你的xcloc文件所在的文件夹
input_dir = "/Users/nhuji/Desktop/Fruta Localizations"

# 这是你想要将解压缩的xliff文件保存到的文件夹
output_dir = "/Users/nhuji/Desktop/Fruta Localizations Tepm"

# 遍历文件夹中的所有文件
for filename in os.listdir(input_dir):
    # 检查文件是否是xcloc文件
    if filename.endswith(".xcloc"):
        # 创建一个新的文件夹来保存这个xcloc文件中的xliff文件
        new_dir = os.path.join(output_dir, filename[:-6])  # 去掉".xcloc"后缀
        os.makedirs(new_dir, exist_ok=True)

        # 找到xcloc文件中的xliff文件
        for root, dirs, files in os.walk(os.path.join(input_dir, filename)):
            for file in files:
                if file.endswith(".xliff"):
                    # 将xliff文件复制到新的文件夹中
                    shutil.copy(os.path.join(root, file), new_dir)
