# Powered by: Ing. Jorge Contreras
# Fecha: 31/08/2015

from django.forms import ModelForm
from django import forms
from .models import *

class clientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        help_texts = {
            'name': 'Ex: John Doe',
            'address': 'Ex: 1313 Mockinberg Lane',
            'city': 'Ex: Duluth'
        }

class packageForm(ModelForm):
    class Meta:
        model = Package
        exclude = ('operator','client','reciever','tracking','currentState')

class recieverForm(ModelForm):
    class Meta:
        model = Receiver
        fields = '__all__'