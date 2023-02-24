from django.forms import ModelForm
from .models import Morador


class MoradorForm(ModelForm):
    class Meta:
        model = Morador
        fields = '__all__'


class NovoMoradorForm(ModelForm):
    class Meta:
        model = Morador
        fields = '__all__'
