from django.urls import path

from goods import views  #импорт views из goods для регистрации функций

app_name = 'goods'
urlpatterns = [
    path('search/', views.catalog, name='search'),
    path('<slug:category_slug>/', views.catalog, name='index'), #регистрируем страницу каталога
    path('product/<slug:product_slug>/', views.product, name='product'),
    # path('get-product-id/', views.get_product_id, name='get-product-id'),
] # site/catalog/...
