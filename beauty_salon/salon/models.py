from django.db import models
from django.contrib.auth.models import User

# Модель для клиентов
class Buyer(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    phone_number = models.IntegerField()
    spent_money = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


# Модель для услугS
class Service(models.Model):
    objects = models.ManyToManyField
    title = models.CharField(max_length=255)
    description = models.TextField(db_default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

# Модель для работ (проектов)
class Work(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='works/')
    description = models.TextField()

    def __str__(self):
        return self.name

# Модель для статей
class Article(models.Model):
    objects = models.Manager
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Модель для контактов
class Contact(models.Model):
    objects = models.Manager
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    address = models.CharField(max_length=255)


    def __str__(self):
        return self.address
