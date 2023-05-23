import os
import json
import xml.etree.ElementTree as ET

# 这是你的JSON文件的位置
input_file = "/Users/nhuji/Desktop/Fruta Localizations JSON/translations.json"

# 这是你想要将新的xliff文件保存到的文件夹
output_dir = "/Users/nhuji/Desktop/Fruta Localizations XLIFF"

# 从JSON文件中读取数据
with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 确保输出文件夹存在
os.makedirs(output_dir, exist_ok=True)

# 为每种语言创建一个新的xliff文件
for language_code in data[list(data.keys())[0]].keys():
    if language_code in ['source', 'note']:
        continue

    # 创建一个新的xliff根元素
    root = ET.Element(
        'xliff', {'version': '1.2', 'xmlns': 'urn:oasis:names:tc:xliff:document:1.2'})

    # 创建一个新的file元素
    file = ET.SubElement(root, 'file', {'original': 'Localizable.strings',
                         'source-language': 'en', 'target-language': language_code, 'datatype': 'plaintext'})

    # 创建一个新的body元素
    body = ET.SubElement(file, 'body')

    # 为每个翻译添加一个新的trans-unit元素
    for id, translation in data.items():
        # 创建一个新的trans-unit元素
        trans_unit = ET.SubElement(body, 'trans-unit', {'id': id})

        # 创建一个新的source元素
        source = ET.SubElement(trans_unit, 'source')
        source.text = translation['source']

        # 创建一个新的target元素
        target = ET.SubElement(trans_unit, 'target')
        target.text = translation.get(
            language_code, "")  # 使用get方法，如果键不存在，返回空字符串

        # 创建一个新的note元素
        note = ET.SubElement(trans_unit, 'note')
        note.text = translation['note']

    # 将新的xliff文件保存到文件中
    tree = ET.ElementTree(root)
    tree.write(os.path.join(
        output_dir, f'{language_code}.xliff'), encoding='utf-8', xml_declaration=True)
