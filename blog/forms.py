from dataclasses import fields
from django.forms import ModelForm
from .models import *

class DogForm(ModelForm):
    class Meta:
        model = Dog
        fields = '__all__'

class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'