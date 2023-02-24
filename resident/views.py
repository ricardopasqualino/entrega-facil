from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .form import MoradorForm, NovoMoradorForm
from .models import Morador


@login_required
def resident_index(request):
    return render(request, 'resident/home.html')


@login_required
def moradores(request):
    morador = Morador.objects.all()
    data = {'morador': morador}
    return render(request, 'resident/moradores.html', data)


@login_required
def criar_morador(request):
    novo_morador = Morador.objects.all()
    form = NovoMoradorForm()
    data = {'novo_morador': novo_morador, 'form': form}
    return render(request, 'resident/criar-morador.html', data)


@login_required
def cta_criar_morador(request):
    form = NovoMoradorForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('moradores')


@login_required
def atualizar_morador(request, id):
    data = {}
    atualizar_morador = Morador.objects.get(id=id)
    form = NovoMoradorForm(request.POST or None, instance=atualizar_morador)
    data['atualizar_morador'] = atualizar_morador
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('moradores')
    else:
        return render(request, 'resident/atualizar-morador.html', data)


@login_required
def remover_morador(request, id):
    remover_morador = Morador.objects.get(id=id)
    if request.method == 'POST':
        remover_morador.delete()
        return redirect ('moradores')
    else:
        return render (request, 'resident/remover-morador.html', {'remover_morador' : remover_morador})