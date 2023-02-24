from __future__ import absolute_import, unicode_literals
from celery import shared_task

from delivery.models import Morador, Delivery

app = Delivery


@shared_task
def add (x ,y):
    return x + y 


@shared_task
def mul(x,y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


def entrega_nova(Morador):
    email = Morador.email
    if Morador.aceite_alertas is True
        print('enviar o email para esse morador')
    else:
        print('Não enviar email para o morador!')


def entrega_retirada():
    return ('A entrega ', Delivery.nota_fiscal, 'foi retirada pelo ', Morador.nome)
