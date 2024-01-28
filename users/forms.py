from django import forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import User

class UserLoginForm(AuthenticationForm): #наследуемся от специальной функции для работы с формами аутентификации   
    class Meta:
        model = User #модель с которой работаем
    
    username = forms.CharField()
    password = forms.CharField()

#настраиваем форму аутентификации
#далее связать с views.py

    # class UserLoginForm(AuthenticationForm): #наследуемся от специальной функции для работы с формами аутентификации   
    # username = forms.CharField(
    #     label= 'Имя пользователя',
    #     widget=forms.TextInput(attrs={"autofocus": True,
    #                                                         'class':'form-control',
    #                                                         'placeholder':'Введите имя пользователя'}),
    # )
    # password = forms.CharField(
    #     label= 'Пароль',
    #     widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
    #                                       'class':'form-control',
    #                                         'placeholder':'Введите пароль'}),
    # )
    
    # class Meta:
    #     model = User #модель с которой работаем

#настраиваем форму аутентификации
#далее связать с views.py