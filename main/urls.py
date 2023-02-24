from django.contrib import admin # Importa o modulo de login do Django
from django.urls import include, path # Importa as funções do path e include

from main.views import (
    index,
    perfil,
    painel,
)

urlpatterns = [
    path('', index , name='main_index'),
    path('perfil/', perfil, name='main_perfil'),
    path('painel/', painel , name='main_painel'),
]