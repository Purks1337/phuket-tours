import os

# --- КОНФИГУРАЦИЯ ---

# Имя файла, в который будет записан результат
OUTPUT_FILE = "context.md"

# Папки, которые нужно включить в парсинг (и дерево, и, возможно, контент)
# ОБЪЕДИНИЛ в один список, чтобы ничего не перезаписывалось
DIRS_TO_INCLUDE = ["src", "public"]

# Папки из списка выше, для которых нужно строить ТОЛЬКО дерево, 
# но НЕ читать содержимое файлов (например, статика, картинки)
DIRS_TREE_ONLY = ["public"]

# Папки, которые нужно полностью исключить из парсинга
DIRS_TO_EXCLUDE = [
    ".git",
    ".astro",
    ".idea",
    ".vscode",
    ".next",
    "node_modules",
    "__pycache__",
    "dist",
    "build",
    "coverage",
]

# Файлы, которые нужно исключить из парсинга
FILES_TO_EXCLUDE = [
    os.path.basename(__file__),
    OUTPUT_FILE,
    ".DS_Store",
    ".env",
    ".env.local",
    "package-lock.json",
    "yarn.lock",
    "pnpm-lock.yaml",
]

# Расширения файлов, которые считаются бинарными (на всякий случай)
BINARY_EXTENSIONS = [
    '.png', '.jpg', '.jpeg', '.gif', '.ico', '.svg', '.eot', '.ttf', '.woff',
    '.woff2', '.pyc', '.lock', '.zip', '.gz', '.pdf', '.doc', '.docx', '.mp4', '.mov', '.webm'
]
# --- КОНЕЦ КОНФИГУРАЦИИ ---


def is_binary(filepath):
    """Проверяет, является ли файл бинарным по его расширению."""
    return any(filepath.lower().endswith(ext) for ext in BINARY_EXTENSIONS)

def get_tree(startpath):
    """Генерирует строковое представление структуры проекта."""
    tree_lines = ["# Структура проекта\n\n```"]
    
    # 1. Файлы в корне
    for item in sorted(os.listdir(startpath)):
        path = os.path.join(startpath, item)
        if os.path.isfile(path):
            if item not in FILES_TO_EXCLUDE and not is_binary(item):
                tree_lines.append(f"📄 {item}")

    # 2. Папки, которые нужно включить
    for include_dir in DIRS_TO_INCLUDE:
        full_include_path = os.path.join(startpath, include_dir)
        
        # Если папка существует, добавляем её в дерево
        if os.path.isdir(full_include_path):
            tree_lines.append(f"📁 {include_dir}/")
            
            for root, dirs, files in os.walk(full_include_path, topdown=True):
                # Исключаем ненужные подпапки
                dirs[:] = [d for d in dirs if d not in DIRS_TO_EXCLUDE]
                
                # Сортируем
                dirs.sort()
                files.sort()

                level = root.replace(full_include_path, '').count(os.sep)
                indent = '    ' * level + '│   '

                for d in dirs:
                    tree_lines.append(f"{indent}📁 {d}/")
                for f in files:
                    if f not in FILES_TO_EXCLUDE:
                        # В дереве показываем файл, даже если он бинарный (просто имя),
                        # но можно добавить условие not is_binary(f), если хотим скрыть их из дерева.
                        tree_lines.append(f"{indent}📄 {f}")
    
    tree_lines.append("```\n")
    return "\n".join(tree_lines)


def get_file_contents():
    """Собирает содержимое всех релевантных файлов."""
    all_contents = ["# Содержимое файлов\n"]
    files_to_process = []

    # 1. Собираем файлы из корня
    for item in sorted(os.listdir(".")):
        path = os.path.join(".", item)
        if os.path.isfile(path):
            if item not in FILES_TO_EXCLUDE and not is_binary(item):
                files_to_process.append(path)

    # 2. Собираем файлы из включенных папок
    for include_dir in DIRS_TO_INCLUDE:
        # !!! ИЗМЕНЕНИЕ: Если папка в списке "Только дерево", пропускаем чтение контента
        if include_dir in DIRS_TREE_ONLY:
            continue

        if os.path.isdir(include_dir):
            for root, dirs, files in os.walk(include_dir, topdown=True):
                dirs[:] = [d for d in dirs if d not in DIRS_TO_EXCLUDE]
                for f in sorted(files):
                     if f not in FILES_TO_EXCLUDE and not is_binary(f):
                        files_to_process.append(os.path.join(root, f))
    
    # 3. Читаем и форматируем содержимое
    for filepath in files_to_process:
        relative_path = os.path.relpath(filepath, ".").replace('\\', '/')
        all_contents.append(f"\n---\n")
        all_contents.append(f"## ` {relative_path} `\n")
        
        _, extension = os.path.splitext(filepath)
        lang_hint = extension.lstrip('.') if extension else ''
        
        all_contents.append(f"```{lang_hint}")
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                if not content.strip():
                    all_contents.append("(Файл пустой)")
                else:
                    all_contents.append(content)
        except Exception as e:
            all_contents.append(f"Не удалось прочитать файл: {e}")
        all_contents.append("```\n")
        
    return "\n".join(all_contents)


def main():
    print("🚀 Начинаю сборку контекста проекта...")
    try:
        tree_structure = get_tree(".")
        file_contents = get_file_contents()
        
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write(tree_structure)
            f.write("\n")
            f.write(file_contents)
            
        print(f"✅ Контекст проекта успешно создан в файле '{OUTPUT_FILE}'")
        
    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")

if __name__ == "__main__":
    main()