from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render
from goods.models import Products
from goods.utils import q_search
# Create your views here.


def catalog(request, category_slug=None):
    
    page = request.GET.get('page', 1) # если значение по ключу page получить не удастся, то присвоится 1
    on_sale = request.GET.get('on_sale', None) # если значение отсутствует, вернуть None
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)
    #ловим запросы из url адреса.
    
    if category_slug == 'all':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug)) ## get_list_or_404 - стр404 если категория пуста
    if on_sale: #скидка
        goods = goods.filter(discount__gt=0) #если есть on_sale добавить фильтр (discount больше чем 0)
    if order_by and order_by!='default': #сортировка
        goods = goods.order_by(order_by) #если есть order_by и не выбран пункт по умолчанию - добавить фильтр (order_by)
    

    paginator = Paginator(goods, 3) #отображать по 3 товара из переменной goods
    current_page = paginator.page(int(page))

    context = {
        "title": "Home - Каталог",
        "goods": current_page,
        "slug_url": category_slug #для пагинации в catalog.html
    }
    return render(request, "goods/catalog.html", context)

def product(request, product_slug):
    
    product = Products.objects.get(slug=product_slug)
    
    context = {
        "title": "Home - Товар",
        "product": product,
    }
    return render(request, "goods/product.html", context=context)
