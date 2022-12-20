from pyexpat import model
from django import forms 
from .models import CrearEvento
from django.contrib.auth.forms import UserCreationForm

class CrearEventoForm (forms.ModelForm):
    fecha = forms.DateField(widget= forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control', 
                       'placeholder': 'Select a date',
                       'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                      }))

    class Meta:
        model = CrearEvento
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    pass