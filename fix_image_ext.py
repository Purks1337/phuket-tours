import os
import re

images_dir = 'src/assets/images/excursions'
md_dir = 'src/content/excursions'

# Get all valid images
valid_images = {}
for img in os.listdir(images_dir):
    name, ext = os.path.splitext(img)
    valid_images[name] = ext

for md_file in os.listdir(md_dir):
    if not md_file.endswith('.md'): continue
    slug = md_file[:-3]
    filepath = os.path.join(md_dir, md_file)
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Try to find exactly what extension it should be
    if slug in valid_images:
        correct_ext = valid_images[slug]
        correct_cover = f"../../assets/images/excursions/{slug}{correct_ext}"
        
        # Replace the cover line
        new_content = re.sub(r'cover: ".*?"', f'cover: "{correct_cover}"', content)
        if new_content != content:
            with open(filepath, 'w') as f:
                f.write(new_content)
            print(f"Fixed cover for {slug}")

print("Done fixing covers.")
