from django.contrib import admin

from guests.models import ( 
    convidado, 
    lista_convidado, 
    evento, 
    visita,
    local_evento
    )


class ConvidadoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'documento', 'veiculo', 'anfitriao', 'autorizar_convidado']


class ListaConvidadoAdmin(admin.ModelAdmin):
    list_display = ['nome_lista']


class VisitaAdmin(admin.ModelAdmin):
    list_display = ['data', 'convidado', 'anfitriao_visita']


class EventoAdmin(admin.ModelAdmin):
    list_display = ['data_evento', 'qtd_convidados', 'local_eventos']


admin.site.register(convidado, ConvidadoAdmin)
admin.site.register(lista_convidado, ListaConvidadoAdmin)
admin.site.register(evento, EventoAdmin)
admin.site.register(visita, VisitaAdmin)
admin.site.register(local_evento)
