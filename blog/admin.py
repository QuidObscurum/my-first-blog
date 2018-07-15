from django.contrib import admin
from .models import Post 
# Точка перед models означает текущую директорию/приложение. 
# мы можем использовать точку . и имя файла (без расширения .py). https://tutorial.djangogirls.org/ru/dynamic_data_in_templates/
# Register your models here.

admin.site.register(Post)