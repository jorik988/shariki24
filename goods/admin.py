from django.contrib import admin
from goods.forms import SetProductInline
from goods.models import BaseProducts, Categories, Products

#admin.site.register(Categories) Простой способ регистрации таблицы в админ панели

# Register your models here.
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)} # поля для автозаполнения (здесь slug)
    list_display = ['name',] #указываем поля для отображения в админ панели
#регистрируем таблицу Categories в админ панели

@admin.register(BaseProducts)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)} # поля для автозаполнения (здесь slug)
    list_display = ['name', 'description', 'image', 'price',] #указываем поля для отображения в админ панели
#регистрируем таблицу Categories в админ панели

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name', 'quantity', 'price', 'discount', 'image',] #указываем поля для отображения в админ панели
    list_editable = ['quantity', 'discount',] #поля с возможностью быстрого изменения
    search_fields = ['name', 'description', 'id'] #добавляем поиск 
    list_filter = ['quantity', 'price', 'discount', 'category'] #фильтрация
    inlines = [SetProductInline]
    fields = [
        "name",
        "category",    
        "slug",
        "description",
        "image",
        #("price", "discount"),
        "quantity",
    ] #отображение продукта
