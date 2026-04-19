import os
import zipfile
import xml.etree.ElementTree as ET
import json
import re

namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
directory = 'Каталоги Пхукет'
out_images_dir = 'src/assets/images/excursions'
os.makedirs(out_images_dir, exist_ok=True)

results = []

for filename in os.listdir(directory):
    if not filename.endswith('.docx'): continue
    filepath = os.path.join(directory, filename)
    slug = filename.replace('.docx', '').replace(' ', '-').lower()
    slug = re.sub(r'[^a-z0-9\-а-я]', '', slug)
    if not slug:
        slug = f"doc-{len(results)}"
        
    extracted_image = None
    text_content = []
    
    with zipfile.ZipFile(filepath) as docx:
        # Extract text
        doc_xml = docx.read('word/document.xml')
        root = ET.fromstring(doc_xml)
        for paragraph in root.iter(f"{{{namespaces['w']}}}p"):
            texts = [node.text for node in paragraph.iter(f"{{{namespaces['w']}}}t") if node.text]
            if texts:
                text_content.append(''.join(texts))
                
        # Extract one image
        infolist = docx.infolist()
        media_files = [item for item in infolist if item.filename.startswith('word/media/')]
        if media_files:
            media_files.sort(key=lambda x: x.filename)
            first_image_obj = media_files[0]
            first_image_data = docx.read(first_image_obj.filename)
            ext = os.path.splitext(first_image_obj.filename)[1]
            out_img_name = f"{slug}{ext}"
            out_img_path = os.path.join(out_images_dir, out_img_name)
            
            with open(out_img_path, 'wb') as f:
                f.write(first_image_data)
            extracted_image = f"../../assets/images/excursions/{out_img_name}"
            
    results.append({
        "original_file": filename,
        "slug": slug,
        "image": extracted_image,
        "text": "\n".join(text_content)
    })

with open("dump.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"Processed {len(results)} docx files.")
