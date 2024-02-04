from email import message
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm

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
                messages.success(request, f"{user.username}, вы успешно вошли в аккаунт!")
                
                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):#если есть ключ next перенаправлять на страницу из ключа страница не logout
                    return HttpResponseRedirect(request.POST.get('next'))
                    
                return HttpResponseRedirect(reverse('main:index'))#иначе на главную
               
    else:   
        form = UserLoginForm()  #иначе (если был Get) просто открыть страницу авторицаии

    context = {
        "title": "Home - Авторизация",
        'form': form,
        
    }
    return render(request, 'users/login.html', context=context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request. POST)
        if form.is_valid():
            form.save()
            user =form.instance #берем данные из формы чтобы сразу залогиниться
            auth.login(request, user) #логинимся сразу после регистрации
            messages.success(request, f"{user.username}, вы успешно зарегистрировались!")
            return HttpResponseRedirect (reverse('main:index'))
    else:   
        form = UserRegistrationForm()
    
    context = {
        "title": "Home - Регистрация",
        'form': form,    
    }
    return render(request, 'users/registration.html', context=context)

@login_required #запрет для незарег. пользоваиелей
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request. POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Профиль успешно обновлен!")
            return HttpResponseRedirect (reverse('user:profile'))
    else:   
        form = ProfileForm(instance=request.user)
    
    context = {
        "title": "Home - Профиль",
        'form': form,
    }
    return render(request, 'users/profile.html', context=context)

@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, вы вышли из акаунта.")
    auth.logout(request)
    return redirect(reverse('main:index'))

def users_cart(request):
    
    return render(request, 'users/users_cart.html')


