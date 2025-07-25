
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    '''Главная страница'''
    context = {
        'title': 'Страховая платформа',
        'message': 'VIP проект успешно запущен!'
    }
    return render(request, 'main/index.html', context)

def about(request):
    '''Страница о компании'''
    return render(request, 'main/about.html')

def contacts(request):
    '''Страница контактов'''
    return render(request, 'main/contacts.html')
