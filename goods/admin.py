from django.contrib import admin
from django.utils.safestring import mark_safe
from goods.forms import CategoriesInline, SetProductInline
from goods.models import BaseProducts, Categories, Products

#admin.site.register(Categories) Простой способ регистрации таблицы в админ панели

# Register your models here.
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)} # поля для автозаполнения (здесь slug)
    list_display = ['name',] #указываем поля для отображения в админ панели


@admin.register(BaseProducts)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)} # поля для автозаполнения (здесь slug)
    list_display = ['name', 'description', 'image', 'price',] #указываем поля для отображения в админ панели


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug':('name',)}
    list_display = ['name', 'product_photo_min', 'price', 'discount', 'quantity', 'id',] #указываем поля для отображения в админ панели
    list_editable = ['quantity', 'discount',] #поля с возможностью быстрого изменения
    search_fields = ['name', 'description', 'id'] #добавляем поиск 
    list_filter = ['quantity', 'price', 'discount','category'] #фильтрация
    filter_horizontal = ['category']  # Позволяет выбирать несколько категорий
    inlines = [SetProductInline]
    save_on_top = False
    readonly_fields = ['product_photo', ]
    fields = [
        "name",
        "category",    
        #"slug",
        "description",
        ("price", "discount"),
        "image",
        "product_photo",
        
    ]
    @admin.display(description="Изображение", ordering='content')
    def product_photo_min (self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=80>")
        else: 
            return f'Нет фото'
    @admin.display(description="Просмотр", ordering='content')
    def product_photo (self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=350>")
        else: 
            return f'Нет фото'
    class Media:
        js = ('goods/prepopulate_name.js',)  # Для автозаполнения name