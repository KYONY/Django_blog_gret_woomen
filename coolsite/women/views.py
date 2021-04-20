from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }

    return render(request, 'women/index.html', context=context)


# def about(request):
#     return render(request, 'women/index.html', {'menu': menu, 'title': 'О сайте'})


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    """Обработка страницы добавления контента"""
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()

            return redirect('home')
    else:
        form = AddPostForm()

    return render(request, 'women/addpage.html', {'menu': menu, 'title': 'Добавление статьи', 'form': form})


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")



def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    # post = get_object_or_404(Women, pk=post_id)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'women/post.html', context=context)


def show_category(request, cat_slug):
    posts = Women.objects.filter(cat__slug=cat_slug)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_slug,
    }

    return render(request, 'women/index.html', context=context)

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


# def show_post(request, post_id):
#     return HttpResponse(f"Отображение статьи с id = {post_id}")


# def archive(request, year):
# 	"""Функция с обработкой исключения 404"""
# 	if (int(year) > 2020):
# 		raise Http404()
# 	return HttpResponse(f"<h1>Архив по годам</h1>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
