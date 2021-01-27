from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^lista-usario/$', views.UsuarioList.as_view({'get': 'list', 'post': 'create'}), name='posts-list'),
    
]