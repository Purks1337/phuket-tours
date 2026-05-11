import json
import re

with open('dump.json', 'r') as f:
    data = json.load(f)

slugs = ['carnival-magic', 'fantasea', 'jet-ski-по-островам', 'siam-niramit', 'simon-cabaret', 'аквапарк-andamanda', 'дайвинг', 'дельфинарий', 'зиплайн-парк-эраван', 'катание-на-квадроциклах-и-багги', 'тайский-бокс']

for item in data:
    if item['slug'] in slugs:
        text = item['text']
        print(f"=== {item['slug']} ===")
        # Print only lines containing price identifiers
        for line in text.split('\n'):
            if re.search(r'\d{3,4}', line) and ('бат' in line or '-' in line or '–' in line or '/' in line):
                print(line)
