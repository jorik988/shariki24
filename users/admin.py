from django.contrib import admin
from carts.admin import CartTabAdmin
from users.models import User

#admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email',] #указываем поля для отображения в админ панели
    inlines = [CartTabAdmin,] #показ корзины пользователя
#регистрируем таблицу  в админ панели