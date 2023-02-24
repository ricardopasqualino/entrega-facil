from django.contrib import admin # Importa o modulo de login do Django
from django.urls import include, path # Importa as funções do path e include

from delivery.views import ( 
    Home, 
    Casa, 
    Morador,
    Nova, 
    Entrega_nova, 
    Entregas, 
    Atualizar_entrega,
    Erro,
)

urlpatterns = [
    path('delivery/', Home, name='delivery_home'),
    path('casa/', Casa, name='Casa'),
    path('morador/', Morador, name='Morador'),
    path('nova/', Nova , name='Nova'),
    path('entrega-nova/', Entrega_nova , name='Entrega_nova'),
    path('atualizar-entrega-<id>/', Atualizar_entrega , name='Atualizar_entrega'),
    path('entregas/', Entregas , name='Entregas'),
    path('erro/', Erro , name='Erro'),
]