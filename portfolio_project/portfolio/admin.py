from django.contrib import admin
from .models import Project

# регистрируем модели, которые хотим видет в админке командой:
admin.site.register(Project)
