from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('saludo', views.saludo, name='saludo'),
    re_path('^.*$', views.index),
]
