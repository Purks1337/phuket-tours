import zipfile
import re
import os
import xml.etree.ElementTree as ET

namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
directory = 'Каталоги Пхукет'

for filename in os.listdir(directory):
    if not filename.endswith('.docx'): continue
    filepath = os.path.join(directory, filename)
    with zipfile.ZipFile(filepath) as docx:
        doc_xml = docx.read('word/document.xml')
        root = ET.fromstring(doc_xml)
        text = []
        for paragraph in root.iter(f"{{{namespaces['w']}}}p"):
            texts = [node.text for node in paragraph.iter(f"{{{namespaces['w']}}}t") if node.text]
            if texts:
                text.append(''.join(texts))
        
        full_text = '\n'.join(text)
        # Search for lines containing numbers that look like prices
        price_lines = [line for line in full_text.split('\n') if 'стоимост' in line.lower() or 'цена' in line.lower() or 'price' in line.lower() or '/' in line]
        
        candidates = []
        for line in price_lines:
            nums = re.findall(r'\b\d{3,4}\b', line)
            if len(nums) >= 4:
                candidates.append(line)
        if candidates:
            print(f"--- {filename} ---")
            for c in candidates:
                print("  ", c)
