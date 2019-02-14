from django.urls import re_path
from . import views

app_name = 'users'
urlpatterns = [
    re_path('register/', views.register, name='register'),
    re_path('login/', views.login, name='login'),

]
