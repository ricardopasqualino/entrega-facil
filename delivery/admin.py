from django.contrib import admin


from delivery.models import ( 
    Delivery, 
    Box,
    Moradia,
    )


class DeliveryAdmin(admin.ModelAdmin):
    list_display = [
                    'nota_fiscal',
                    'data_entrada',
                    'data_retirada', 
                    'recebido_por', 
                    'modulo', 
                    'status',
                    'id', 
                    ]



admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(Box)
admin.site.register(Moradia)