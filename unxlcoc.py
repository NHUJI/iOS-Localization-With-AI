import os
import json
import xml.etree.ElementTree as ET

# 这是你的xcloc文件所在的文件夹
input_dir = "/Users/nhuji/Desktop/Kingdom Companion Localizations"

# 这是你想要将解析出的数据保存为JSON的文件夹
output_dir = "/Users/nhuji/Desktop/Kingdom Companion Localizations JSON"

# 创建一个字典来保存所有的数据
data = {}

# 遍历文件夹中的所有文件
for filename in os.listdir(input_dir):
    # 检查文件是否是xcloc文件
    if filename.endswith(".xcloc"):
        # 获取语言代码
        language_code = filename[:-6]  # 去掉".xcloc"后缀

        # 找到xcloc文件中的xliff文件
        for root, dirs, files in os.walk(os.path.join(input_dir, filename)):
            for file in files:
                if file.endswith(".xliff"):
                    # 解析xliff文件
                    tree = ET.parse(os.path.join(root, file))
                    root = tree.getroot()

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

                        # 如果这个id还没有在数据字典中，就添加一个新的条目
                        if id not in data:
                            data[id] = {'source': source, 'note': note}

                        # 将这种语言的翻译添加到数据字典中
                        data[id][language_code] = target

# 将字典转换为JSON格式，并保存到文件中
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, 'translations.json'), 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
