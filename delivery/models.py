# import das bibliotecas
from django.db import models
from django.contrib.auth.models import User


# import dos arquivos
from resident.models import Moradia


class Box(models.Model):
    box = models.CharField(max_length=10, default=None, null=False)

    def __str__(self):
        return self.box


class Delivery(models.Model):
    nota_fiscal = models.CharField(max_length=15, default=None, null=False, blank=False, verbose_name='Nota Fiscal')
    morador = models.ForeignKey(Moradia, on_delete=models.DO_NOTHING)
    modulo = models.ForeignKey(Box, on_delete=models.DO_NOTHING)
    recebido_por = models.ForeignKey(User, on_delete=models.DO_NOTHING) 
    status = models.BooleanField(null=False, default=False)
    data_entrada = models.DateTimeField(null=False, blank=False, auto_now_add=True, unique_for_date=True)
    data_retirada = models.DateTimeField(auto_now=status)


    def __str__(self):
        return self.nota_fiscal


class Profile(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    telefone = models.CharField(max_length=15, default=None, null=True)

    def __str__(self):
        return self.usuario
