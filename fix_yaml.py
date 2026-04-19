import re
import os

fixes = {
    "аквапарк-andamanda": """---
title: "Аквапарк Andamanda"
category: "НЕОБЫЧНЫЕ"
priceAdult: 1450
priceChild: 1300
childAge: "90-120 см"
pricePrefix: "от"
cover: "../../assets/images/excursions/аквапарк-andamanda.jpeg"
packages:
  - title: "Без трансфера"
    priceAdult: 1450
    priceChild: 1300
    childAge: "90-120 см"
  - title: "С трансфером"
    priceAdult: 1850
    priceChild: 1700
    childAge: "90-120 см"
---""",
    "зиплайн-парк-эраван": """---
title: "Зиплайн-парк Эраван"
category: "НАЗЕМНЫЕ"
priceAdult: 1800
pricePrefix: "от"
cover: "../../assets/images/excursions/зиплайн-парк-эраван.jpeg"
packages:
  - title: "Зиплайн 42 платформы"
    priceAdult: 3000
  - title: "Зиплайн 20 платформ"
    priceAdult: 2100
  - title: "Зиплайн 17 платформ"
    priceAdult: 2100
  - title: "Зиплайн 12 платформ"
    priceAdult: 1800
  - title: "42 платформы + Квадроцикл (30 мин)"
    priceAdult: 3700
    priceChild: 3400
  - title: "42 платформы + Квадроцикл (60 мин)"
    priceAdult: 4300
    priceChild: 3700
---""",
    "дельфинарий": """---
title: "Дельфинарий"
category: "НЕОБЫЧНЫЕ"
priceAdult: 700
priceChild: 400
childAge: "4-11 лет"
pricePrefix: "от"
cover: "../../assets/images/excursions/дельфинарий.jpeg"
packages:
  - title: "VVIP (ряд A)"
    priceAdult: 1200
    priceChild: 700
  - title: "VIP (ряд B)"
    priceAdult: 1000
    priceChild: 600
  - title: "Deluxe (ряды C–D)"
    priceAdult: 900
    priceChild: 500
  - title: "Regular (ряды E–G)"
    priceAdult: 700
    priceChild: 400
---""",
    "тайский-бокс": """---
title: "Тайский бокс"
category: "НЕОБЫЧНЫЕ"
priceAdult: 1500
pricePrefix: "от"
cover: "../../assets/images/excursions/тайский-бокс.jpeg"
packages:
  - title: "У ринга"
    priceAdult: 1800
  - title: "Амфитеатр"
    priceAdult: 1500
---""",
    "siam-niramit": """---
title: "Siam Niramit"
category: "НЕОБЫЧНЫЕ"
priceAdult: 1600
priceChild: 1400
childAge: "100-140 см"
pricePrefix: "от"
cover: "../../assets/images/excursions/siam-niramit.png"
packages:
  - title: "Silver (только шоу)"
    priceAdult: 1600
    priceChild: 1400
  - title: "Gold (только шоу)"
    priceAdult: 1700
    priceChild: 1500
  - title: "Platinum (только шоу)"
    priceAdult: 1800
    priceChild: 1600
  - title: "Silver (шоу + ужин)"
    priceAdult: 1800
    priceChild: 1600
  - title: "Gold (шоу + ужин)"
    priceAdult: 1900
    priceChild: 1700
  - title: "Platinum (шоу + ужин)"
    priceAdult: 2000
    priceChild: 1800
---""",
    "катание-на-квадроциклах-и-багги": """---
title: "Катание на квадроциклах и багги"
category: "НАЗЕМНЫЕ"
priceAdult: 800
priceChild: 600
pricePrefix: "от"
cover: "../../assets/images/excursions/катание-на-квадроциклах-и-багги.jpeg"
packages:
  - title: "Квадроциклы 30 минут"
    priceAdult: 800
    priceChild: 600
  - title: "Квадроциклы 60 минут"
    priceAdult: 1800
    priceChild: 1300
  - title: "Квадроциклы 90 минут"
    priceAdult: 2300
    priceChild: 1600
  - title: "Багги 30 минут"
    priceAdult: 1600
    priceChild: 1000
  - title: "Багги 60 минут"
    priceAdult: 2400
    priceChild: 1800
---""",
    "fantasea": """---
title: "Остров фантазий FantaSea"
category: "НЕОБЫЧНЫЕ"
priceAdult: 1800
pricePrefix: "от"
cover: "../../assets/images/excursions/fantasea.jpeg"
packages:
  - title: "Только шоу"
    priceAdult: 1800
  - title: "Шоу + ужин"
    priceAdult: 2200
    priceChild: 2000
    childAge: "90-140 см"
---""",
    "simon-cabaret": """---
title: "Simon Cabaret"
category: "НЕОБЫЧНЫЕ"
priceAdult: 700
priceChild: 600
pricePrefix: "от"
childAge: "90-120 см"
cover: "../../assets/images/excursions/simon-cabaret.png"
packages:
  - title: "Балкон"
    priceAdult: 700
    priceChild: 600
  - title: "Партер"
    priceAdult: 900
    priceChild: 800
---""",
    "jet-ski-по-островам": """---
title: "Jet Ski по островам"
category: "МОРСКИЕ"
priceAdult: 5000
pricePrefix: "от"
cover: "../../assets/images/excursions/jet-ski-по-островам.png"
packages:
  - title: "Гидроцикл Yamaha (до 2-х чел) – англ. гид"
    priceAdult: 5000
  - title: "Гидроцикл Sea-doo (до 2-х чел) – англ. гид"
    priceAdult: 5200
  - title: "Гидроцикл Yamaha (до 2-х чел) – рус. гид"
    priceAdult: 5400
---""",
    "carnival-magic": """---
title: "Carnival Magic"
category: "НЕОБЫЧНЫЕ"
priceAdult: 2100
priceChild: 2100
pricePrefix: "от"
childAge: "до 140 см"
cover: "../../assets/images/excursions/carnival-magic.jpeg"
packages:
  - title: "Только шоу"
    priceAdult: 2100
    priceChild: 2100
  - title: "Шоу + ужин"
    priceAdult: 2500
    priceChild: 2400
---""",
    "дайвинг": """---
title: "Дайвинг на Пхукете"
category: "МОРСКИЕ"
priceAdult: 3300
pricePrefix: "от"
cover: "../../assets/images/excursions/дайвинг.jpeg"
packages:
  - title: "Сопровождающий (без погружения)"
    priceAdult: 3300
  - title: "2 погружения на Рача Яй"
    priceAdult: 3500
  - title: "3 погружения (Рача Яй + Рача Ной)"
    priceAdult: 4500
---"""
}

for slug, new_frontmatter in fixes.items():
    filepath = f"src/content/excursions/{slug}.md"
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            content = f.read()
            
        new_content = re.sub(r'^---(.*?)---\n', new_frontmatter + '\n', content, flags=re.DOTALL)
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Fixed {slug}")

print("Done.")
