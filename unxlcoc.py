import os
import json
import xml.etree.ElementTree as ET

# 这是你的xcloc文件所在的文件夹
input_dir = "/Users/nhuji/Desktop/Fruta Localizations"

# 这是你想要将解析出的数据保存为JSON的文件夹
output_dir = "/Users/nhuji/Desktop/Fruta Localizations JSON"

# 遍历文件夹中的所有文件
for filename in os.listdir(input_dir):
    # 检查文件是否是xcloc文件
    if filename.endswith(".xcloc"):
        # 创建一个新的文件夹来保存这个xcloc文件中的JSON文件
        new_dir = os.path.join(output_dir, filename[:-6])  # 去掉".xcloc"后缀
        os.makedirs(new_dir, exist_ok=True)

        # 找到xcloc文件中的xliff文件
        for root, dirs, files in os.walk(os.path.join(input_dir, filename)):
            for file in files:
                if file.endswith(".xliff"):
                    # 解析xliff文件
                    tree = ET.parse(os.path.join(root, file))
                    root = tree.getroot()

                    # 创建一个字典来保存解析出的数据
                    data = {}

                    # 遍历xliff文件中的所有trans-unit元素
                    for trans_unit in root.iter('{urn:oasis:names:tc:xliff:document:1.2}trans-unit'):
                        # 获取id、source、target和note元素的文本
                        id = trans_unit.get('id')
                        source = trans_unit.find(
                            '{urn:oasis:names:tc:xliff:document:1.2}source').text
                        target_element = trans_unit.find(
                            '{urn:oasis:names:tc:xliff:document:1.2}target')
                        target = target_element.text if target_element is not None else ""
                        note = trans_unit.find(
                            '{urn:oasis:names:tc:xliff:document:1.2}note').text

                        # 将这些数据添加到字典中
                        data[id] = {'source': source,
                                    'target': target, 'note': note}

                    # 将字典转换为JSON格式，并保存到文件中
                    with open(os.path.join(new_dir, file[:-6] + '.json'), 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=4)
