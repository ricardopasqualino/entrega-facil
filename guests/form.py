from django.forms import ModelForm
from .models import evento, convidado


class NovoEventoForm(ModelForm):
    class Meta:
        model = evento
        fields = '__all__'


class NovoVisitanteForm(ModelForm):
    class Meta:
        model = convidado
        fields = '__all__'
