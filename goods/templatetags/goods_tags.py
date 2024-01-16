from django import template
from goods.models import Categories

register = template.Library()

@register.simple_tag() #регистрируем функцию как тег для вызова в шаблонах
def tag_categories():
    return Categories.objects.all()
#создаем функцию которая возвращает все объекты из таблицы категории


