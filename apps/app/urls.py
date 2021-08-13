from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/v1/saludo', views.saludo, name='saludo'),
    path('api/v1/login', views.login, name='login'),
    re_path('^.*$', views.index),
]
