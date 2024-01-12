
from django.urls import path

from main import views  #импорт views из main для регистрации функций

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'), #регистрируем главную страницу
    path('about/', views.about, name='about'), #регистрируем страницу about
    path('contacts/', views.contacts, name='contacts'), #регистрируем страницу contacts
    path('delivery/', views.delivery, name='delivery')
]

