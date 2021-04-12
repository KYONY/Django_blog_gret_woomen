from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *


menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def index(request):
	posts = Women.objects.all()
	return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def about(request):
	return render(request, 'women/index.html', {'menu': menu, 'title': 'О сайте'})


# def catigories(request, catid):
# 	if request.GET:
# 		print(request.GET)
# 		print(request.GET['name'])
# 	return HttpResponse(f'<h1>Статьи по категориям </h1><p>{catid}</p>')


# def archive(request, year):
# 	"""Функция с редиректом, permanent=True -- создает 301 редирект, без данного параметра - 302"""
# 	if (int(year) > 2020):
# 		return redirect('home', permanent=True)
# 	return HttpResponse(f"<h1>Архив по годам</h1>{year}</p>")


# def archive(request, year):
# 	"""Функция с обработкой исключения 404"""
# 	if (int(year) > 2020):
# 		raise Http404()
# 	return HttpResponse(f"<h1>Архив по годам</h1>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
