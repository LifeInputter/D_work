from flask import render_template
from app import app, db
from app.models import Service, Work, Article, Contact

# Маршрут для страницы http://127.0.0.1:5000
@app.route("/")
def start_page():
    return render_template("base.html")

# Маршрут для страницы "О нас"
@app.route("/about")
def about():
    return render_template("about.html")

# Маршрут для страницы "Наши услуги"
@app.route("/services")
def services():
    services = Service.query.all()
    return render_template("services.html", services=services)

# Маршрут для страницы "Наши работы"
@app.route("/works")
def works():
    works = Work.query.all()
    return render_template("works.html", works=works)

# Маршрут для страницы "Статьи"
@app.route("/articles")
def articles():
    articles = Article.query.all()
    return render_template("articles.html", articles=articles)

# Маршрут для страницы "Контакты"
@app.route("/contacts")
def contacts():
    contact_info = Contact.query.first()
    return render_template("contacts.html", contact_info=contact_info)


