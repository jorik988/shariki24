
from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

# Create your views here.

def index(request): #request содержит данные о запросе(инф о пользователе, куки и тд)
       
    context = {
        'title': 'ШарикиНаДом - Главная',
        'content': 'Магазин воздушных шаров ШарикиНаДом.РФ',
    }
    return render(request, 'main/index.html', context)
# Ф-я представления или контроллер

def about(request):
    context = {
        'title': 'ШарикиНаДом - О нас',
        'content': 'Информация о нас',
        'text_on_page': 'Здесь будет информация о нас',
    }
    return render(request, 'main/about.html', context)

def contacts(request):
    context = {
        'title': 'ШарикиНаДом - Контакты',
        'content': 'Контакты',
        'text_on_page': 'Здесь будет контактная информация.',
    }
    return render(request, 'main/contacts.html', context)

def delivery(request):
    context = {
        'title': 'ШарикиНаДом - Доставка',
        'content': 'Доставка',
        'text_on_page': 'Здесь будет информация о доставке',
    }
    return render(request, 'main/delivery.html', context)
