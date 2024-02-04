from django import template
from carts.models import Cart

register = template.Library()

@register.simple_tag() #регистрируем функцию как тег для вызова в шаблонах
def user_carts(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)