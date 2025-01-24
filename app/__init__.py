from flask import Flask

app = Flask(
    __name__,
    template_folder="../templates",  # Убедитесь, что пути верные
    static_folder="../static"
)

from app import routes  # Импорт маршрутов

