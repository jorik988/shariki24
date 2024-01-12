
from django.urls import path

from goods import views  #импорт views из main для регистрации функций

app_name = 'goods'
urlpatterns = [
    path('', views.catalog, name='catalog'), #регистрируем главную страницу
    path('product/', views.product, name='product'), #регистрируем страницу about

]
