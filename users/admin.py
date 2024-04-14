from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from carts.admin import CartTabAdmin
from orders.admin import OrderTabulareAdmin
from users.models import User

#admin.site.register(User)

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email',] #указываем поля для отображения в админ панели
    inlines = [CartTabAdmin,OrderTabulareAdmin] #показ корзины пользователя
#регистрируем таблицу  в админ панели