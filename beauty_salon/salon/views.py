from django.shortcuts import render
from .models import Service, Work, Article, Contact
from .forms import CommentForm
from django.http import HttpResponse
from django.views.decorators.http import require_POST
import os

# Create your views here.


def main(request):
    title = 'Салон красоты "Оазис"'
    link1 = "Войти в личный кабинет/ Зарегистрироваться"

    context = {
        'title': title,
        'link1': link1
    }
    return render(request, 'main_page.html', context)

def about_page(request):
    return render(request, 'about.html')

def services_page(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def works_page(request):
    works = "Лучшие работы"
    works = Work.objects.all()
    # works = []
    # for file in os.listdir('static/works'):
    #     if file.endswith(('.jpg', '.png', '.gif')):
    #         works.append({'image': f'static/works/{file}'})
    context = {
        'works': works
        }
    return render(request, 'works_page.html', {'works': works})

def blogs(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})

def contacts(request):
    contact_info = Contact.objects.first()
    return render(request, 'contacts.html', {'contact': contact_info})

# views.py

def comment_form_view(request):
    form = CommentForm()
    return render(request, 'comment_form.html', {'form': form})

@require_POST
def submit_comment(request):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save()
        return HttpResponse('<script>window.opener.location.reload(); window.close();</script>')
    else:
        return render(request, 'comment_form.html', {'form': form})

