from django.db import models
from django.contrib.auth.models import User


class Condominio(models.Model):
    nome = models.CharField(max_length=50, default=None,null=True, verbose_name='Nome do condominio')

    def __str__(self):
        return self.nome


class Moradia(models.Model):
    numero_moradia = models.CharField(max_length=4, default=None, null=True, verbose_name='Número da casa')

    def __str__(self):
        return self.numero_moradia


class Morador(models.Model):
    nome = models.CharField(max_length=200, default=None, null=True)
    sobrenome = models.CharField(max_length=200, default=None, null=True)
    telefone = models.CharField(max_length=40, default=None, null=True)
    email = models.CharField(max_length=200, default=None, null=True, verbose_name='E-mail')
    morador = models.ForeignKey(Moradia, on_delete=models.DO_NOTHING, default=None)
    condominio = models.ForeignKey(Condominio, on_delete=models.DO_NOTHING, verbose_name='Nome do condomínio')

    def __str__(self):
        return self.nome
    