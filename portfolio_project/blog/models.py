from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=300)  # в скобках создаем отображение данного атрибута, ограничеие по кол-ву символов
    description = models.TextField()  # короткое описание проекта
    date = models.DateField()
# Create your models here.

    def __str__(self): # чтобы в админке мы видели все
        return self.title

