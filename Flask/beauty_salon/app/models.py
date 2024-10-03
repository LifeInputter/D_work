from app import db

# Модель для услуг
class Service(db.Model):
    __tablename__ = "services"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)

# Модель для работ
class Work(db.Model):
    __tablename__ = "works"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(255), nullable=False)

# Модель для статей
class Article(db.Model):
    __tablename__ = "articles"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.String(255), nullable=False)

# Модель для контактов
class Contact(db.Model):
    __tablename__ = "contacts"
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    opening_hours = db.Column(db.Text, nullable=False)
