from django.shortcuts import render
from .models import Project
def home(request):
    # ВСЕГО ЛИШЬ ОДНА СТРОКА ИМПОРТИРУЕТ ВСЕ БАЗЫ ДАННЫХ, КОНВЕРТИРУЯ ОБЪЕКТЫ В ПАЙТОН И ДОБАВЛЯЕТ ИХ В СПИСОК:
    projects = Project.objects.all() # получаем данные, так джанго импортирует все данные из базы данных
    return render(request, 'portfolio/home.html', {'projects': projects}) # передаем запрос а затем название шаблона, используя переменную projects передаем словарь в шаблон где ключом будет projects а значением список projects который мы сейчас создали
# Create your views here.
# Джанго это полный баланс между автоматизацией и кодированием в ручную
