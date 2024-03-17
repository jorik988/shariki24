from django import template
from carts.utils import get_user_carts

register = template.Library()

@register.simple_tag() #регистрируем функцию как тег для вызова в шаблонах
def user_carts(request):
    return get_user_carts(request)