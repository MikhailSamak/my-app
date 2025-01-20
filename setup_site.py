import os

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
        "styles.css"  # CSS для стилизации
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
from flask import render_template

@app.route("/")
def home():
    return render_template("base.html")
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
        <h1>Welcome to the AI Interface</h1>
    </header>
    <main>
        <p>This is a modern interface for your AI project. Let's make it amazing!</p>
    </main>
    <footer>
        <p>Developed by Aira</p>
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

main {
    padding: 2rem;
    text-align: center;
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
