from django.contrib import admin
from .models import Blog

# регистрируем модели, которые хотим видет в админке командой:
admin.site.register(Blog)

# Register your models here.
