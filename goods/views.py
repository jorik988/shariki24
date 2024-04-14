from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render
from goods.models import Products, SetProduct
from goods.utils import  q_search

# Create your views here.


def catalog(request, category_slug=None):
    
    page = request.GET.get('page', 1) # если значение по ключу page получить не удастся, то присвоится 1
    on_sale = request.GET.get('on_sale', None) # если значение отсутствует, вернуть None
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)
    #ловим запросы из url адреса.
    
    goods = Products.objects.all()   
    if category_slug == 'all':
        pass
    elif query:
        goods = q_search(query)
    else:
        goods = goods.filter(category__slug=category_slug)
    if on_sale: #скидка
        goods = goods.filter(discount__gt=0) #если есть on_sale добавить фильтр (discount больше чем 0)
    if order_by and order_by!='default': #сортировка
        goods = goods.order_by(order_by) #если есть order_by и не выбран пункт по умолчанию - добавить фильтр (order_by)
    

    paginator = Paginator(goods, 50) #отображать по 50 товаров из переменной goods
    current_page = paginator.page(int(page))

    context = {
        "title": "мойшарик.рф - Каталог",
        "goods": current_page,
        "slug_url": category_slug, #для пагинации в catalog.html
        "is_category_page": True #для отображения нужных элементов только на странице каталога
    }
    return render(request, "goods/catalog.html", context)

def product(request, product_slug):
    
    product = Products.objects.get(slug=product_slug)
    base_products = product.base_products.all().order_by('name')
    total_base_product = base_products.count()
    base_products_with_quantities = [(bp, SetProduct.objects.filter(product=product, base_product=bp).first().quantity) for bp in base_products]
    
    context = {
        "title": "мойшарик.рф - Товар",
        "product": product,
        #"base_products": base_products,
        "total_base_product": total_base_product,
        "base_products_with_quantities": base_products_with_quantities
        
    }
    return render(request, "goods/product.html", context=context)
