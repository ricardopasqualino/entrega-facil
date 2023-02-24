from django.contrib import admin # Importa o modulo de login do Django
from django.urls import include, path # Importa as funções do path e include


from resident.views import (
    resident_index,
    moradores,
    criar_morador,
    cta_criar_morador,
    remover_morador,
    atualizar_morador,
)


urlpatterns = [
    path('resident-home/', resident_index , name='resident_index'),
    path('moradores/', moradores, name='moradores'),

    path('criar-morador/', criar_morador, name='criar_morador'),
    path('cta_criar-morador/', cta_criar_morador, name='cta_criar_morador'),
    
    path('atualizar-morador/(?P<id>\d+)/$', atualizar_morador, name='atualizar_morador'),
    path('remover-morador/(?P<id>\d+)/$', remover_morador, name='remover_morador'),

]