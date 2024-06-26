from carts.models import Cart


def get_user_carts(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user).select_related('product') #фильтруем корзины по user
    if not request.session.session_key:
        request.session.create() #если не авторизован, создать ключ сессии
        
    return Cart.objects.filter(session_key=request.session.session_key).select_related('product')#фильтруем по ключу сессии