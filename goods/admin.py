from django.contrib import admin
from goods.models import Categories, Products

#admin.site.register(Categories) Простой способ регистрации таблицы в админ панели

# Register your models here.
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)} # поля для автозаполнения (здесь slug)
    list_display = ['name',] #указываем поля для отображения в админ панели
#регистрируем таблицу Categories в админ панели

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name', 'quantity', 'price', 'discount',] #указываем поля для отображения в админ панели
    list_editable = ['quantity', 'discount',] #поля с возможностью быстрого изменения
    search_fields = ['name', 'description', 'id'] #добавляем поиск 
    list_filter = ['quantity', 'price', 'discount', 'category'] #фильтрация
    fields = [
        "name",
        "category",
        "slug",
        "description",
        "image",
        ("price", "discount"),
        "quantity",
    ] #отображение продукта