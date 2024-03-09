from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser): # создаем таблицу для БД
    image = models.ImageField(upload_to='users_images' ,blank=True, null=True, verbose_name='Аватар')
    phone_number = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'user' # изменяем название таблицы в БД
        verbose_name: str = 'Пользователь' # изменяем название таблицы в админ панели
        verbose_name_plural = 'Пользователи'
    def __str__(self):
        return f'{self.username}'