from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request): #request содержит данные о запросе(инф о пользователе, куки и тд)
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели Home',

    }
    return render(request, 'main/index.html', context)
# Ф-я представления или контроллер

def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'Информация о нас',
        'text_on_page': 'Здесь будет информация о нас',
    }
    return render(request, 'main/about.html', context)

def contacts(request):
    context = {
        'title': 'Home - Контакты',
        'content': 'Контакты',
        'text_on_page': 'Здесь будет контактная информация.',
    }
    return render(request, 'main/contacts.html', context)

def delivery(request):
    context = {
        'title': 'Home - Доставка',
        'content': 'Доставка',
        'text_on_page': 'Здесь будет информация о доставке',
    }
    return render(request, 'main/delivery.html', context)
