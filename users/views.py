from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import UserLoginForm

def login(request):
    if request.method == 'POST': #если был пост запрос авторизовываем пользователя
        form = UserLoginForm(data=request. POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            #проверяем что пользователь есть в базе
            if user: #если данные совпали то логинемся
                auth.login (request, user)
                return HttpResponseRedirect (reverse('main:index'))
    else:   
        form = UserLoginForm()  #иначе (если был Get) просто открыть страницу авторицаии

    context = {
        "title": "Home - Авторизация",
        'form': form,
        
    }
    return render(request, 'users/login.html', context=context)


def registration(request):
    
    context = {
        "title": "Home - Регистрация",
        
    }
    return render(request, 'users/registration.html', context=context)

def profile(request):
    
    context = {
        "title": "Home - Профиль",
        
    }
    return render(request, 'users/profile.html', context=context)


def logout(request):
    ...