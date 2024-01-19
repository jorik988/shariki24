from django import template
from django.utils.http import urlencode
from goods.models import Categories

register = template.Library()

@register.simple_tag() #регистрируем функцию как тег для вызова в шаблонах
def tag_categories():
    return Categories.objects.all()
#создаем функцию которая возвращает все объекты из таблицы категории

@register.simple_tag(takes_context=True)
def change_params (context, **kwargs) -> str:
    query = context['request'].GET.dict()
    query.update (kwargs)
    return urlencode(query)
# функция объединяет get запросы фильтрации и пагинации