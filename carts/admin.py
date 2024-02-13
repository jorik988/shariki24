
from dataclasses import fields
from django.contrib import admin
from carts.models import Cart


#admin.site.register(Cart)

class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = 'product', 'quantity', 'created_timestamp',
    search_fields = 'product','quantity', 'created_timestamp',
    readonly_fields = ('created_timestamp',)
    extra = 1
# для отображения корзины в инфо о пользовалете в админ панели

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user_display', 'product_display', 'quantity', 'created_timestamp',] #указываем поля для отображения в админ панели
    list_filter = ['created_timestamp', 'user', 'product__name',]
    list_editable = ['quantity',]
    
    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return "Анонимный пользователь"
    
    def product_display(self, obj):
        
        return str(obj.product.name)
        

    