from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', (WomenHome.as_view()), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(extra_context={'title': "Список по категориям"}), name='category'),
    path('logout/', logout_user, name='logout'),

    # path('', cache_page(60)(WomenHome.as_view()), name='home'),
    # path('addpage/', addpage, name='add_page'),
    # path('login/', login, name='login'),
    # path('', index, name='home'),
    # path('post/<slug:post_slug>/', show_post, name='post'),
    # path('category/<slug:cat_slug>/', show_category, name='category'),

    # path('category/<int:cat_id>/', show_category, name='category'),
    # path('post/<int:post_id>/', show_post, name='post'),
    # path('cats/<int:catid>/', catigories),
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]