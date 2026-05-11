import zipfile
import re
import os
import sys
import xml.etree.ElementTree as ET

def get_docx_text_and_image(filepath, extract_dir):
    text = []
    first_image = None
    namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    
    with zipfile.ZipFile(filepath) as docx:
        # Get text
        doc_xml = docx.read('word/document.xml')
        root = ET.fromstring(doc_xml)
        for paragraph in root.iter(f"{{{namespaces['w']}}}p"):
            texts = [node.text for node in paragraph.iter(f"{{{namespaces['w']}}}t") if node.text]
            if texts:
                text.append(''.join(texts))
                
        # Get first image
        infolist = docx.infolist()
        media_files = [item for item in infolist if item.filename.startswith('word/media/')]
        if media_files:
            # Sort to get something like image1.jpeg
            media_files.sort(key=lambda x: x.filename)
            first_image_obj = media_files[0]
            first_image_data = docx.read(first_image_obj.filename)
            ext = os.path.splitext(first_image_obj.filename)[1]
            out_img_name = os.path.basename(filepath).replace('.docx', '') + ext
            out_img_path = os.path.join(extract_dir, out_img_name)
            
            os.makedirs(extract_dir, exist_ok=True)
            with open(out_img_path, 'wb') as f:
                f.write(first_image_data)
            first_image = out_img_path

    return '\n'.join(text), first_image

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python parse_docx.py <path_to_docx>")
        sys.exit(1)
        
    p = sys.argv[1]
    txt, img = get_docx_text_and_image(p, 'extracted_media')
    print("IMAGE:", img)
    print("TEXT:")
    print(txt[:2000]) # print first 2000 chars

