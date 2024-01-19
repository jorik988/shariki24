
from django.urls import path

from goods import views  #импорт views из main для регистрации функций

app_name = 'goods'
urlpatterns = [
    path('<slug:category_slug>/', views.catalog, name='index'), #регистрируем страницу каталога
    path('product/<slug:product_slug>/', views.product, name='product'), 

]
