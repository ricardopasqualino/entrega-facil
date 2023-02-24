from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .form import NovoEventoForm, NovoVisitanteForm
from .models import convidado, evento, lista_convidado


@login_required
def guest_home(request):
    return render(request, 'guests/home.html')


@login_required
def visitantes(request):
    visitante = convidado.objects.all()
    data = {'visitante' : visitante}
    return render (request, 'guests/convidados.html', data)


# mandar a url do form para validar o novo visitante cadastrado.
def novo_visitante(request):
    form = NovoVisitanteForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('guests_convidado')


# Página para o acesso e criação de um novo convidado
def criar_visitante(request):
    evento_dados = convidado.objects.all()
    form = NovoVisitanteForm()
    data = {'evento_dados' : evento_dados, 'form' : form }
    return render(request, 'guests/convidado-criar.html', data)


@login_required
def atualizar_visitante(request, id):
    data = {}
    atualizar_visitante = convidado.objects.get(id=id)
    form = NovoVisitanteForm(request.POST or None, instance=atualizar_visitante)
    data['atualizar_visitante'] = atualizar_visitante
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('guests_convidado')
    else:
        return render(request, 'guests/convidado-editar.html', data)


def deletar_visitante(request, id):
    deletar_visitante = convidado.objects.get(id=id)
    if request.method == 'POST':
        deletar_visitante.delete()
        return redirect('guests_convidado')
    else:
        return render (request, 'guests/convidado-deletar.html', {'deletar_visitante' : deletar_visitante})


@login_required
def listas(request):
    listas = lista_convidado.objects.all()
    data = {'listas' : listas}
    return render (request, 'guests/listas.html', data)


@login_required
def eventos(request):
    evento_dados = evento.objects.order_by('data_evento').all()
    form = NovoEventoForm()
    data = {'evento_dados' : evento_dados, 'form' : form }
    return render (request, 'guests/eventos.html', data)


@login_required
def criar_evento(request):
    evento_dado = evento.objects.all()
    form = NovoEventoForm()
    data = {'evento_dado' : evento_dado, 'form' : form }
    return render(request, 'guests/evento-criar.html', data)


@login_required
def atualizar_evento(request, id):
    data = {}
    atualizar_evento = evento.objects.get(id=id)
    form = NovoEventoForm(request.POST or None, instance=atualizar_evento)
    data['atualizar_evento'] = atualizar_evento
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('guests_evento')
    else:
        return render(request, 'guests/evento-editar.html', data)


def deletar_evento(request, id):
    deletar_evento = evento.objects.get(id=id)
    if request.method == 'POST':
        deletar_evento.delete()
        return redirect ('guests_evento')
    else:
        return render (request, 'guests/evento-deletar.html', {'deletar_evento' : deletar_evento})



# Função para validar o cadastro de um novo evento
@login_required
def novo_evento(request):
    form = NovoEventoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('guests_evento')
