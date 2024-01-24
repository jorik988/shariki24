
from django.urls import path

from users import views  #импорт views из main для регистрации функций

app_name = 'users'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    
    
]
