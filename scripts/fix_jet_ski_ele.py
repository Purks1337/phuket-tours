import re
import os

filepath = 'src/content/excursions/jet-ski-со-слонами.md'

if os.path.exists(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    new_content = re.sub(r'title: ".*?"', 'title: "Jet Ski со слонами"', content, count=1)
    with open(filepath, 'w') as f:
        f.write(new_content)
    print("Fixed Jet Ski Elephants")
