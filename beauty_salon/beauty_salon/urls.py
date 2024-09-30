"""
URL configuration for beauty_salon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from salon.views import main,about_page,services_page,works_page, blogs, contacts, comment_form_view, submit_comment
# from beauty_salon.salon.views import main, about_page, services_page,works_page, blogs, contacts
# from .views import about_view, services_view, works_view, articles_view, contacts_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='home'),
    path('about/', about_page, name='about'),
    path('services/', services_page, name='services'),
    path('works/', works_page, name='works'),
    path('articles/', blogs, name='articles'),
    path('contacts/', contacts, name='contacts'),
    path('comment-form/', comment_form_view, name='comment_form'),
    path('submit-comment/', submit_comment, name='submit_comment'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)