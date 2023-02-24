from django.forms import ModelForm
from .models import Delivery


class NovaForm(ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__' 


class DeliveryForm(ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__' 