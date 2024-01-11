from shlex import join
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request): #request содержит данные о запросе(инф о пользователе, куки и тд)
    return render(request, 'main/index.html')
# Ф-я представления или контроллер

def about(request):
    return HttpResponse('About page')