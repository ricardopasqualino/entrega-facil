from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from delivery.models import Delivery
from resident.models import Morador, Moradia


def index(request):
    return render(request, 'main/home.html')


@login_required
def perfil(request):
    return render(request, 'main/perfil.html')


@login_required
def painel(request):
    entregas = Delivery.objects.filter(status=0)
    entregas_total = Delivery.objects.all().count()
    entregas_pendentes = Delivery.objects.filter(status=0).count()
    entregas_retiradas = Delivery.objects.filter(status=1).count()
    qtd_morador = Morador.objects.all().count()
    qtd_casas = Moradia.objects.all().count()
    data = {'entregas_total': entregas_total, 
            'entregas_pendentes': entregas_pendentes, 
            'entregas_retiradas':entregas_retiradas,
            'entregas':entregas, 
            'qtd_morador':qtd_morador,
            'qtd_casas':qtd_casas}
    return render(request, 'main/painel.html', data)