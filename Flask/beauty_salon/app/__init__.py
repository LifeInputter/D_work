from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Инициализация приложения Flask и базы данных SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../beauty_salon.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Импортируем маршруты
from app.routes import *

# Создаем таблицы базы данных, если они не существуют
with app.app_context():
    db.create_all()
