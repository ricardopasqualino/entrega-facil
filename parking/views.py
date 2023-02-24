from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from parking.models import vagas

def parking_home(resquest):
    return render(resquest, 'parking/home.html')


@login_required
def consultar_vagas(request):
    vaga = vagas.objects.all()
    data = {'vaga' : vaga}
    return render(request, 'parking/vagas.html', data)


@login_required
def reservar_vagas(request):
    return render (request, 'parking/reservar-vagas.html')
