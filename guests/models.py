from django.db import models

from resident.models import Morador


class convidado(models.Model):
    data_visita = models.DateField(default=None)
    hora_visita = models.TimeField(default=None)
    nome = models.CharField(max_length=300, default=None, null=True)
    sobrenome = models.CharField(max_length=300, default=None, null=True)
    documento = models.CharField(max_length=100, default=None, null=True)
    cpf = models.CharField(max_length=100, default=None, null=True)
    veiculo = models.CharField(max_length=100, default=None, null=True)
    anfitriao = models.ForeignKey(Morador, on_delete = models.DO_NOTHING)
    autorizar_convidado = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.nome


class lista_convidado(models.Model):
    nome_lista = models.CharField(max_length=100, default=None, null=False, blank=False)
    convidados_lista = models.ManyToManyField(convidado)

    def __str__(self):
        return self.nome_lista


class visita(models.Model):
    data = models.DateTimeField(null=False, blank=False)
    convidado = models.ForeignKey(convidado, on_delete = models.CASCADE)
    anfitriao_visita = models.ForeignKey(Morador, on_delete=models.DO_NOTHING, default=None)

    def __str__(self):
        return self.convidado


class local_evento(models.Model):
    nome_local = models.CharField(max_length=20, default=None, blank=False, null=False)

    def __str__(self):
        return self.nome_local


class evento(models.Model):
    nome_evento = models.CharField(max_length=20, default=None)
    data_evento = models.DateTimeField(null=False, blank=False, default=None)
    qtd_convidados = models.CharField(max_length=3, default=None, null=False, blank=False)
    local_eventos = models.ForeignKey(local_evento, on_delete=models.DO_NOTHING, default=None)
    convidados_evento = models.ManyToManyField(convidado)
    aceite_condicoes = models.BooleanField(default=False, blank=False, null=False)

    def __str__(self):
        return self.nome_evento
