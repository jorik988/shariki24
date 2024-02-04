from django.urls import path

from carts import views  #импорт views из goods для регистрации функций

app_name = 'carts'
urlpatterns = [
    path('cart_add/<slug:product_slug>', views.cart_add, name='cart_add'),
    path('cart_change/<slug:product_slug>', views.cart_change, name='cart_change'),
    path('cart_remove/<slug:product_slug>', views.cart_remove, name='cart_remove'),
]
