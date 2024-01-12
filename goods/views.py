from django.shortcuts import render

# Create your views here.

def catalog(request):
    context = {
        'title': 'Home - Каталог',
    }
    return render(request, 'goods/catalog.html', context)

def product(request):
    context = {
        'title': 'Home - Товар',
    }
    return render(request, 'goods/product.html', context)
