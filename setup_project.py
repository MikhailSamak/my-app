import os

# Укажите корневую папку проекта
project_root = "C:\\AI\\AI_Projects\\site_project"

# Структура папок и файлов
folders_and_files = {
    "app": [
        "__init__.py",
        "routes.py"
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

@app.route("/")
def home():
    return \"Hello, Flask!\"
""")
                    elif file == "requirements.txt":
                        f.write("flask\n")

# Создаем структуру проекта
create_project_structure(project_root, folders_and_files)

print(f"Проект создан в {project_root}")
