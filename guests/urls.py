from django.contrib import admin # Importa o modulo de login do Django
from django.urls import include, path # Importa as funções do path e include

from guests.views import (
    visitantes, 
    eventos, 
    listas, 
    guest_home, 
    novo_evento, 
    criar_evento, 
    novo_visitante,
    criar_visitante,
    atualizar_evento,
    atualizar_visitante,
    deletar_visitante,
    deletar_evento,
)

urlpatterns = [

    path('guests/', guest_home , name='guests_home'),
    path('convidados/', visitantes , name='guests_convidado'),
    path('novo-convidado/', novo_visitante , name='guests_novo_convidado'),
    path('criar-convidado/', criar_visitante , name='guests_criar_convidado'),
    path('atualizar-convidado/(?P<id>\d+)/$', atualizar_visitante , name='guests_editar_convidado'),
    path('deletar-convidado/(?P<id>\d+)/$', deletar_visitante , name='guests_deletar_convidado'),
    path('lista-convidados/', listas , name='guests_lista'),

    path('eventos/', eventos , name='guests_evento'),
    path('novo-evento/', novo_evento , name='guests_novo_evento'),
    path('criar-evento/', criar_evento , name='guests_criar_evento'),
    path('atualizar-evento/(?P<id>\d+)/$', atualizar_evento , name='guests_atualizar_evento'),
    path('deletar-evento/(?P<id>\d+)/$', deletar_evento , name='guests_deletar_evento'),

]