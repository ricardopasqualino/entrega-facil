from django.contrib import admin


from resident.models import ( 
    Morador,
    Condominio, 
    )


class CondominioAdmin(admin.ModelAdmin):
    list_display = ['nome']


class MoradorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sobrenome', 'telefone', 'email']


admin.site.register(Morador, MoradorAdmin)
admin.site.register(Condominio, CondominioAdmin)