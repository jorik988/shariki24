
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request): #request содержит данные о запросе(инф о пользователе, куки и тд)
       
    context = {
        'title': 'мойшарик.рф - Главная',
        'content': 'Магазин воздушных шаров МОЙШАРИК.РФ',
    }
    return render(request, 'main/index.html', context)
# Ф-я представления или контроллер

def about(request):
    context = {
        'title': 'мойшарик.рф - О нас',
    }
    return render(request, 'main/about.html', context)

def contacts(request):
    context = {
        'title': 'мойшарик.рф - Контакты',
    }
    return render(request, 'main/contacts.html', context)

def delivery(request):
    context = {
        'title': 'мойшарик.рф - Доставка',
    }
    return render(request, 'main/delivery.html', context)
