from django.db import models # СДЕСЬ УЖЕ ЕСТЬ ИМПОРТ МОДЕЛЕЙ ДЛЯ ИХ СОЗДАНИЯ

class Project(models.Model): #мы создали класс обеспечивающий взаимодействие с бд в джанго, модель необходима для создания таблиц и ее содержимого

    # создаем атрибуты,необходимая вариация оформления есть в документации:
    title = models.CharField(max_length=100) # в скобках создаем отображение данного атрибута, ограничеие по кол-ву символов
    description = models.CharField(max_length=300) # короткое описание проекта
    image = models.ImageField(upload_to='portfolio/images/') # работаем с рисунками, где можем указать высоту, ширину, размер и т.д.
    url = models.URLField(blank=True)

    def __str__(self): # чтобы в админке мы видели все
        return self.title


