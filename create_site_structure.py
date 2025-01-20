import os
import json

# Укажите корневую папку проекта
project_root = "C:\\AI\\AI_Projects\\site_project"

# Структура папок и файлов
folders_and_files = {
    "app": [
        "__init__.py",
        "routes.py"
    ],
    "memory": [],  # Папка для хранения данных
    "static": [
        "styles.css",  # CSS для стилизации
        "hero_image.jpg"  # Изображение для главной страницы
    ],
    "templates": [
        "base.html"  # Основной HTML шаблон
    ],
    "": [  # Корневая папка
        "run.py",
        "requirements.txt"
    ]
}

# Создаем структуру проекта
def create_project_structure(root, structure):
    for folder, files in structure.items():
        folder_path = os.path.join(root, folder)
        if folder:  # Если это папка, создаем ее
            os.makedirs(folder_path, exist_ok=True)
        for file in files:
            file_path = os.path.join(folder_path, file)
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    # Заполняем файлы шаблоном, если необходимо
                    if file == "run.py":
                        f.write("""from app import app

if __name__ == \"__main__\":
    app.run(debug=True)
""")
                    elif file == "__init__.py":
                        f.write("""from flask import Flask

app = Flask(__name__)

from app import routes
""")
                    elif file == "routes.py":
                        f.write("""from app import app
from flask import render_template, request, jsonify
import os
import json

# Путь к файлу памяти
memory_file_path = os.path.join("memory", "memory_data.json")

# Проверка и создание файла памяти, если его нет
if not os.path.exists(memory_file_path):
    with open(memory_file_path, "w") as memory_file:
        json.dump({"history": [], "settings": {}, "templates": {}, "preferences": {}}, memory_file)

# Функция для чтения памяти
def read_memory():
    with open(memory_file_path, "r") as memory_file:
        return json.load(memory_file)

# Функция для записи в память
def write_memory(data):
    with open(memory_file_path, "w") as memory_file:
        json.dump(data, memory_file, indent=4)

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/memory", methods=["GET", "POST"])
def memory_page():
    if request.method == "POST":
        data = request.json
        if data and "action" in data:
            memory = read_memory()
            memory["history"].append(data["action"])
            write_memory(memory)
            return jsonify({"status": "success", "message": "Данные сохранены"})
        return jsonify({"status": "error", "message": "Нет данных для сохранения"})
    memory = read_memory()
    return render_template("memory.html", memory=memory)
""")
                    elif file == "requirements.txt":
                        f.write("flask\n")
                    elif file == "base.html":
                        f.write("""<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>AI Project</title>
    <link rel=\"stylesheet\" href=\"/static/styles.css\">
</head>
<body>
    <header>
        <h1>Добро пожаловать в интерфейс ИИ</h1>
    </header>
    <main>
        <section class=\"hero\">
            <img src=\"/static/hero_image.jpg\" alt=\"Hero Image\">
            <h2>Этот сайт создан для вас. Будущее начинается здесь!</h2>
            <button>Узнать больше</button>
        </section>
    </main>
    <footer>
        <p>Разработано Айрой</p>
    </footer>
</body>
</html>
""")
                    elif file == "styles.css":
                        f.write("""body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f9;
    color: #333;
}

header {
    background-color: #6200ea;
    color: white;
    padding: 1rem 0;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.hero {
    text-align: center;
    padding: 2rem;
    background-color: #e3f2fd;
}

.hero img {
    max-width: 100%;
    height: auto;
    border-radius: 10px;
    margin-bottom: 1rem;
}

.hero button {
    background-color: #6200ea;
    color: white;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1rem;
}

.hero button:hover {
    background-color: #3700b3;
}

footer {
    margin-top: 2rem;
    padding: 1rem 0;
    text-align: center;
    background-color: #6200ea;
    color: white;
}
""")

# Создаем структуру проекта
create_project_structure(project_root, folders_and_files)

print(f"Проект создан в {project_root}")


