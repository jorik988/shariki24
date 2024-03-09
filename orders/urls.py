from django.urls import path

from orders import views  #импорт views из goods для регистрации функций

app_name = 'orders'
urlpatterns = [
    path('create-order/', views.create_order, name='create_order'),
]
