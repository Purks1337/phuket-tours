import json
import re
import os

with open('dump.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

os.makedirs('src/content/excursions', exist_ok=True)

def parse_price_line(line):
    # Try to extract: Name, AdultPrice, ChildPrice, ChildAge
    # 1. 1450/1300 (от 90 до 120 см) – без трансфера
    # 2. Программа 42 платформы + 30 минут катания — 3700 бат (водитель) / 3400 бат (пассажир)
    # 3. VVIP (ряд A) Взрослый — 1200 бат Детский — 700 бат (4–11 лет)
    # 4. Platinum — 1800 / 1600 бат (от 100 до 140 см)
    pass # Will build robust regexes below

for item in data:
    text = item['text']
    slug = item['slug']
    lines = text.split('\n')
    lines = [l.strip() for l in lines if l.strip()]
    
    title = lines[0] if lines else slug
    subtitle = ""
    # if line 2 is short and not price, probably subtitle
    if len(lines) > 1 and "стоимост" not in lines[1].lower() and "цена" not in lines[1].lower() and len(lines[1]) < 60:
        subtitle = lines[1]
        
    prices = []
    packages = []
    
    # Simple heuristic to find categories
    category = "ХИТЫ"
    lower_text = text.lower()
    if 'остров' in lower_text or 'море' in lower_text or 'катер' in lower_text or 'дайвинг' in lower_text:
        category = "МОРСКИЕ"
    if 'джип' in lower_text or 'квадроцикл' in lower_text or 'сафари' in lower_text or 'храм' in lower_text:
        category = "НАЗЕМНЫЕ"
    if 'шоу' in lower_text or 'кабаре' in lower_text or 'аквапарк' in lower_text or 'дельфин' in lower_text:
        category = "НЕОБЫЧНЫЕ"
        
    # Find price lines
    price_parsing_active = False
    overview_index = len(lines)
    
    for i, line in enumerate(lines):
        lline = line.lower()
        if "обзор" in lline or "программа" in lline and i > 4 or "основные моменты" in lline:
            overview_index = i
            break

    header_lines = lines[:overview_index]
    body_lines = lines[overview_index:]
    
    for line in header_lines:
        # Regex to find numbers that look like prices
        nums = re.findall(r'\b(?:[4-9]\d{2}|[1-9]\d{3})\b', line)
        if hasattr(line, 'lower'):
            line_str = line
        else:
            line_str = str(line)
            
        if len(nums) > 0 and ('/' in line_str or 'бат' in line_str.lower() or '–' in line_str or '-' in line_str or '—' in line_str):
            # Probably a price line
            # Default package parsing:
            pkg_title = line_str
            adult = int(nums[0])
            child = int(nums[1]) if len(nums) > 1 else None
            
            # Clean title
            pkg_title = re.sub(r'\b(?:[4-9]\d{2}|[1-9]\d{3})\b', '', pkg_title)
            pkg_title = pkg_title.replace('бат', '').replace('Стоимость:', '').replace('/', '').replace('()', '').replace('-', '').replace('—', '').replace('  ', ' ').strip()
            if not pkg_title:
                pkg_title = "Стандартный вариант"
                
            age_match = re.search(r'\((.*?)\)', line_str)
            child_age = age_match.group(1) if age_match else ""
            
            packages.append({
                "title": pkg_title[:40],
                "priceAdult": adult,
                "priceChild": child,
                "childAge": child_age
            })
            
    # Default prices
    main_adult = 0
    main_child = None
    main_age = ""
    prefix = ""
    if packages:
        packages = sorted(packages, key=lambda x: x["priceAdult"])
        main_adult = packages[0]["priceAdult"]
        main_child = packages[0]["priceChild"]
        main_age = packages[0]["childAge"]
        if len(packages) > 1:
            prefix = "от"
            
    md_content = f"---\n"
    md_content += f"title: \"{title}\"\n"
    if subtitle:
        md_content += f"subtitle: \"{subtitle}\"\n"
    md_content += f"category: \"{category}\"\n"
    if main_adult: md_content += f"priceAdult: {main_adult}\n"
    if main_child: md_content += f"priceChild: {main_child}\n"
    if main_age: md_content += f"childAge: \"{main_age}\"\n"
    if prefix: md_content += f"pricePrefix: \"{prefix}\"\n"
    if item.get("image"): md_content += f"cover: \"{item['image']}\"\n"
    
    if packages and len(packages) > 1:
        md_content += "packages:\n"
        for p in packages:
            md_content += f"  - title: \"{p['title']}\"\n"
            md_content += f"    priceAdult: {p['priceAdult']}\n"
            if p['priceChild']: md_content += f"    priceChild: {p['priceChild']}\n"
            if p['childAge']: md_content += f"    childAge: \"{p['childAge']}\"\n"
            
    md_content += f"---\n\n"
    md_content += "\n\n".join(body_lines)
    
    with open(f"src/content/excursions/{slug}.md", "w", encoding='utf-8') as mf:
        mf.write(md_content)

print("Generated markdown files heuristically.")
