import re
import os

filepath = 'src/content/excursions/рача-корал-2-дня.md'

fix = """---
title: "Рача + Корал на 2 дня"
category: "МОРСКИЕ"
priceAdult: 2800
priceChild: 2600
childAge: "4-10 лет"
pricePrefix: "от"
cover: "../../assets/images/excursions/рача-корал-2-дня.jpeg"
packages:
  - title: "Бунгало с вентилятором"
    priceAdult: 2800
    priceChild: 2600
    childAge: "4-10 лет"
  - title: "Бунгало с кондиционером"
    priceAdult: 3200
    priceChild: 3000
    childAge: "4-10 лет"
---"""

if os.path.exists(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    new_content = re.sub(r'^---(.*?)---\n', fix + '\n', content, flags=re.DOTALL)
    with open(filepath, 'w') as f:
        f.write(new_content)
    print("Fixed Racha")
