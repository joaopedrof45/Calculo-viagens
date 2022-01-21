from django.forms import ModelForm 

from .models import Calculos

class FormCalculo(ModelForm):
     class Meta:
        model = Calculos
        fields = '__all__'
        