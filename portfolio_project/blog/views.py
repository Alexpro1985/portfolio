from django.shortcuts import render, get_object_or_404 # get_object_or_404, либо найдет объект либо отобразит 404 ошибку команда для выгрузки конкретного блога
from .models import Blog
def all_blogs(request):
    # blog_count = Blog.objects.count - это подсчет кол-ва написанных блогов
    blogs = Blog.objects.order_by('-date') # распределение по дате и ограничиваем кол-во постов на странице - [:5] прописываем в конце строки
    return render(request, 'blog/all_blogs.html',{'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id) # передаем имя класса, pk - это термин по работе с базой данных (означает первичный ключ), вообщем эта функция пытается найти объект под нужным номером
    return render(request, 'blog/detail.html', {'blog':blog}) # после этого создаем новый файл html в blog




# Create your views here.
