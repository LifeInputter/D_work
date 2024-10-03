from fastapi import FastAPI, Depends, Request, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from . templating import TemplateResponse
from sqlalchemy import create_engine, Column, Integer, String, Float, Text, insert, select, update, delete
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from fastapi.staticfiles import StaticFiles

# Конфигурация базы данных
SQLALCHEMY_DATABASE_URL = "sqlite:///./beauty_salon.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Инициализация FastAPI
app = FastAPI()

# app.mount("/test", StaticFiles(directory="app/test"), name="test")
app.mount("/static", StaticFiles(directory="app/static"), name="static")
# Шаблоны Jinja2
templates = Jinja2Templates(directory="app/templates")
TemplateResponse = templates.TemplateResponse

# Определение моделей
class Service(Base):
    __tablename__ = "services"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Float, nullable=False)

class Work(Base):
    __tablename__ = "works"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    image = Column(String(255), nullable=False)

class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(String(255), nullable=False)

class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String(20), nullable=False)
    email = Column(String(100), nullable=False)
    address = Column(String(255), nullable=False)
    opening_hours = Column(Text, nullable=False)

# Создание таблиц
Base.metadata.create_all(bind=engine)

# Зависимость для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#Мршрут для страницы «base»
@app.get("/", name = 'about:base_page', response_class=HTMLResponse)
async def base(request: Request):
    return TemplateResponse(request=request, name="base.html")

# Маршрут для страницы «О нас»
@app.get("/about", name = 'about:about_page', response_class=HTMLResponse)
async def about(request: Request):
    return TemplateResponse(request=request, name="about.html")


# Маршрут для страницы «Наши услуги»
@app.get("/services", name = 'services:services_page', response_class=HTMLResponse)
async def services(request: Request, db: Session = Depends(get_db)):
    services = db.query(Service).all()
    context = {
        'services': services
    }
    return TemplateResponse(request=request,name="services.html", context=context)


# Маршрут для страницы «Наши работы»
@app.get("/works", name = 'works:works_page', response_class=HTMLResponse)
async def works(request: Request, db: Session = Depends(get_db)):
    works = db.query(Work).all()
    context = {
        "works": works
    }
    return TemplateResponse(request=request, name="works.html", context=context)


# Маршрут для страницы «Статьи»
@app.get("/articles", name = 'articles:articles_page', response_class=HTMLResponse)
async def articles(request: Request, db: Session = Depends(get_db)):
    articles = db.query(Article).all()
    context = {
        "articles": articles
    }
    return TemplateResponse(request=request, name="articles.html", context=context)


# Маршрут для страницы «Контакты»
@app.get("/contacts", name='contacts:contact_info', response_class=HTMLResponse)
async def contacts(request: Request, db: Session = Depends(get_db)):
    contact_info = db.query(Contact).first()
    context = {
        "contact": contact_info
    }
    return TemplateResponse(request=request, name="contacts.html", context=context)

@app.post("/services")
def create_service(id: int, name: str, description: str, price: int, db: Session = Depends(get_db)):
    services = Service(id=id, name=name, description=description, price=price)
    db.add(services)
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Service has been added'
    }

@app.post("/works")
def create_work(id: int, title: str, description: str, image: str, db: Session = Depends(get_db)):
    works = Work(id=id, title=title, description=description, image=image)
    db.add(works)
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'new work has been created'
    }

@app.post("/articles")
def create_article(id: int, title: str, content: str, created_at: str, db: Session = Depends(get_db)):
    articles = Article(id=id, title=title, content=content, created_at=created_at)
    db.add(articles)
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'new article has been created'
        }

@app.post("/contacts")
def create_contact(id: int, phone: str, email: str, address: str, opening_hours:str, db: Session = Depends(get_db)):
    contacts = Contact(id=id, phone=phone, email=email, address=address, opening_hours=opening_hours)
    db.add(contacts)
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'contact has been created'
        }

@app.put("/services")
def update_Service(id: int, name: str, description: str, price: int, db: Session = Depends(get_db)):
    services = db.scalar(select(Service).where(Service.name == name ))
    # services = db.query(Service).filter(Service.id==id).first()
    if services is not None:
        services.name = name
        services.description = description
        services.price = price
        db.commit()
        new_services = db.execute(update(Service)).where(Service.name == name)
        # new_services = db.query(Service).filter(Service.id == id).first()
        return f'Service was updated {new_services}'
    else:
        return f'Услуги с таким {id} не существует'

@app.put("/works")
def update_Work(id: int, title: str, description: str, image: str, db: Session = Depends(get_db)):
    works = db.query(Service).filter(Service.id == 'id').first()
    # works = db.scalar(select(Work).where(Work.id == id))
    if works is not None:
        works.title = title
        works.description = description
        works.image = image
        db.commit()
        new_works = db.query(Work).filter(Work.id == 'id').first()
        return f'Work was updated {new_works}'
    else:
        return f'Работы с таким {id} не существует'

# Удаление услуги
@app.delete("/services/{service_id}", name='services:delete_service')
def delete_service(service_id: int, db: Session = Depends(get_db)):
    db_service = db.query(Service).filter(Service.id == service_id).first()
    if db_service is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Услуга не найдена")
    db.delete(db_service)
    db.commit()
    return {"message": "Услуга удалена"}

# @app.delete("/works")
# def delete_Work(id: int, db: Session = Depends(get_db)):
#     works = db.query(Work).filter(Work.id == 'id').first()
#     db.delete(works)
#     db.commit()
#     return 'Запись о работе удалена успешно'

# Удаление работы
@app.delete("/works/{work_id}", name='works:delete_work')
def delete_work(work_id: int, db: Session = Depends(get_db)):
    db_work = db.query(Work).filter(Work.id == work_id).first()
    if db_work is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Работа не найдена")
    db.delete(db_work)
    db.commit()
    return {"message": "Работа удалена"}

# Удаление статьи
@app.delete("/articles/{article_id}", name='articles:delete_article')
def delete_article(article_id: int, db: Session = Depends(get_db)):
    db_article = db.query(Article).filter(Article.id == article_id).first()
    if db_article is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Статья не найдена")
    db.delete(db_article)
    db.commit()
    return {"message": "Статья удалена"}

# Удаление контактов
@app.delete("/contacts/{contact_id}", name='contacts:delete_contact')
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    db_contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if db_contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Контакт не найден")
    db.delete(db_contact)
    db.commit()
    return {"message": "Контакт удален"}

# @app.delete("/articles")
# def delete_Article(id: int, db: Session = Depends(get_db)):
#     articles = db.query(Article).filter(Article.id == id).first()
#     db.delete(articles)
#     db.commit()
#     return 'Статья удалена успешно'
