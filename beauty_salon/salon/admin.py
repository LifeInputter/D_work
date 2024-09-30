from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Buyer)
# admin.site.register(Service)
# admin.site.register(Work)
admin.site.register(Article)
admin.site.register(Contact)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'description')
    fields = [('title', 'price'), 'description']
    list_filter = ('title', 'price')

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description')
    fields = [('name', 'image'), 'description']
    list_filter = ('name', 'description')