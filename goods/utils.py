from django.db.models import Q #for search
from goods.models import Products


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    

    keywords = [word for word in query.split() if len(word) > 2]   #создаем список слов из запроса если длина более 2
    q_objects = Q() #создаем переменную для Q объектов
    for token in keywords:
        q_objects |=  Q(description__icontains=token) #наполняем q_object q-объектами по ключевым словам из описания
        q_objects |=  Q(name__icontains=token) #наполняем q_object q-объектами по ключевым словам из названия
    return Products.objects.filter(q_objects) #фильтруем результат