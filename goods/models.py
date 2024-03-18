from django.db import models
from slugify import slugify
from django.urls import reverse
from django.db.models.signals import post_save



# Create your models here.
class Categories(models.Model): # создаем таблицу для БД
    name = models.CharField(max_length=150, unique=True, verbose_name='Название') # поля таблицы CharField тип для текста
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    class Meta:
        db_table = 'category' # изменяем название таблицы в БД
        verbose_name: str = 'Категория' # изменяем название таблицы в админ панели
        verbose_name_plural = 'Категории'
    def __str__(self):
        return f'{self.name}'
    #переопределяем метод что бы изменить название элементов в таблицах в админ панели

class BaseProducts(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название') # поля таблицы CharField тип для текста
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0, decimal_places=0, max_digits=7, verbose_name='Цена')    
    class Meta:
        db_table = 'base_product'
        verbose_name: str = 'Базовый товар'
        verbose_name_plural = 'Базовые товары'
    def __str__(self):
        return f'{self.name}'
    
    def save(self, *args, **kwargs):
        super(BaseProducts, self).save(*args, **kwargs)
        for set_product in self.setproduct_set.all():
            set_product.product.save()
    


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название') # поля таблицы CharField тип для текста
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0, decimal_places=0, max_digits=7, blank=True, null=True, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, decimal_places=2, max_digits=4, blank=True, null=True, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=999, verbose_name='Количество')
    #category = models.ForeignKey(to=Categories, on_delete=models.PROTECT, verbose_name = 'Категория') #ForeignKey связывает товар с категорией
    category = models.ManyToManyField(to=Categories, verbose_name='Категории')
    base_products = models.ManyToManyField(to=BaseProducts, through='SetProduct')
    #PROTECT запрет удаления категории пока в ней есть товары. 
    #CASCADE товары удаляются вместе с категорией
    #SET_DEFAULT, default= товарам будет присвоена категория по умолчанию
    class Meta:
        db_table = 'product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ("id",) #сортировка по умолчанию, чтоб не ругался пагинатор
    def __str__(self):
        return f'{self.name} Количество - {self.quantity}'
    
    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"product_slug": self.slug})
    # получаем url текущего продукта, в админ панели повится кнопка смотреть на сайте
    
    def display_id (self):
        return f'{self.id:05}' # 05 - добавить нули, до 5 знаков (прим id 00007)
    
    def sell_price (self):
        if self.discount:
            return round(self.price - (self.price * self.discount / 100), -1)
        return self.price #если скидки нет вернет обычную цену

    def save(self, *args, **kwargs):
        super(Products, self).save(*args, **kwargs)  # Сначала сохраняем экземпляр Products(или ошибка)
        
        total_price = sum(set_product.base_product.price * set_product.quantity for set_product in self.setproduct_set.all())
        self.price = total_price
            # Обновляем цена по количеству товаров в наборе

        if self.name == "Набор №":
            self.name = f"Набор №{self.id}"
            super(Products, self).save(*args, **kwargs)
        self.slug = slugify(self.name)
        #Заполняем имя по Id, затем заполняем slug


        super(Products, self).save(*args, **kwargs)
        # all_set_products = SetProduct.objects.filter(product=self)
        #     # Получаем все наборы товаров для данного товара Products
        # products_list = [f'{sp.base_product.name} ({sp.quantity} шт.)' for sp in all_set_products]
        #     # Собираем список всех базовых товаров и их количества
        # new_description = ', '.join(products_list)
        #     # Формируем обновленное описание с списком базовых товаров
        # self.description = new_description
        #     # Обновляем описание товара Products
        


class SetProduct(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    base_product = models.ForeignKey(BaseProducts, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество')
        
    def save(self, *args, **kwargs):
        super(SetProduct, self).save(*args, **kwargs)
        # После сохранения SetProduct вызываем пересчет цены у соответствующего товара  
        self.product.save()

