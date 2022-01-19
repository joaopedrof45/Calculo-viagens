from django.forms import ModelForm

from .models import Calculos

class FormCalculo(ModelForm):
     class Meta:
        model = Calculos
        fields = ['numero_protocolo','defensorbool','dias_utei','data_inical','data_final','valor_passagem','valor_translado','cargo','estado','cidade']

