from django.contrib import admin # Importa o modulo de login do Django
from django.urls import include, path # Importa as funções do path e include


from parking.views import (
    reservar_vagas, 
    parking_home, 
    consultar_vagas
)


urlpatterns = [
    path('parking/', parking_home , name='parking_home'),
    path('consultar-vagas/', consultar_vagas , name='parking_consultar_vagas'),
    path('reservar-vaga/', reservar_vagas , name='parking_reservar_vagas'),
]