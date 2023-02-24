from django.db import models

class vagas(models.Model):
    estacionamento = models.CharField(max_length=100, default=None, null=True, blank=True)
    numero_vaga = models.CharField(max_length=100, default=None, null=True, blank=True)
    status_vaga = models.BooleanField(default=False)

    def __str__(self):
        return self.numero_vaga
