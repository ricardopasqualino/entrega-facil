from django.contrib import admin
from parking.models import vagas

class VagaAdmin(admin.ModelAdmin):
    list_display = ['estacionamento', 'numero_vaga', 'status_vaga']

admin.site.register(vagas, VagaAdmin)