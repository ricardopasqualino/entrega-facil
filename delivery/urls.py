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
    f_morador,
    Entregas_pendentes,
)

urlpatterns = [
    path('delivery/', Home, name='delivery_home'),
    path('casa/', Casa, name='Casa'),
    path('morador/', Morador, name='Morador'),
    path('nova/', Nova , name='Nova'),
    path('entregas/', Entregas , name='Entregas'),
    path('entregas-pendentes/', Entregas_pendentes , name='entregas_pendentes'),
    path('entregas/morador/', f_morador , name='f_morador'),
    path('entrega-nova/', Entrega_nova , name='Entrega_nova'),
    path('atualizar-entrega-<id>/', Atualizar_entrega , name='Atualizar_entrega'),
    path('erro/', Erro , name='Erro'),
]