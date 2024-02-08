from django.contrib import admin
from goods.models import Categories, Products

#admin.site.register(Categories) Простой способ регистрации таблицы в админ панели

# Register your models here.
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)} # поля для автозаполнения (здесь slug)
#регистрируем таблицу Categories в админ панели

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name', 'quantity', 'price', 'discount']
