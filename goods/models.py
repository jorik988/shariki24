from email.policy import default
from tabnanny import verbose
from django.db import models

# Create your models here.
class Categories(models.Model): # создаем таблицу для БД
    name = models.CharField(max_length=150, unique=True, verbose_name='Название') # поля таблицы CharField тип для текста
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    class Meta:
        db_table = 'category' # изменяем название таблицы в БД
        verbose_name = 'Категория' # изменяем название таблицы в админ панели
        verbose_name_plural = 'Категории'
    def __str__(self):
        return f'{self.name}'
    #переопределяем метод что бы изменить название элементов в таблицах в админ панели
    
    
#далее создаем миграции manage.py makemigrations
#выполнить миграции в БД manage.py migrate

class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название') # поля таблицы CharField тип для текста
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=7, blank=True, null=True, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, decimal_places=2, max_digits=4, blank=True, null=True, verbose_name='Скидка в %')
    quntity = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT, verbose_name = 'Категория') #ForeignKey связывает товар с категорией
    #PROTECT запрет удаления категории пока в ней есть товары. 
    #CASCADE товары удаляются вместе с категорией
    #SET_DEFAULT, default= товарам будет присвоена категория по умолчанию
    class Meta:
        db_table = 'product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    def __str__(self):
        return f'{self.name} Количество - {self.quntity}'
    
    def display_id (self):
        return f'{self.id:05}' # 05 - добавить нули, до 5 знаков (прим id 00007)
    
    def sell_price (self):
        if self.discount:
            return round(self.price - (self.price * self.discount / 100), 2)
        return self.price #если скидки нет вернет обычную цену
    