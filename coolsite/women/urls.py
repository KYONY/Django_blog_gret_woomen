from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('cats/<int:catid>/', catigories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]