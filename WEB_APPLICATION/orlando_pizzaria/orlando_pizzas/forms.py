from django import forms
from .models import Pizza
from .models import Toppings

class PizzaModelForm (forms.ModelForm):
    class Meta:
        model= Pizza
        fields = ['name','id']
        #The code below tells Django not to generate a label for the text field.
        labels = {'name': ''}

class ToppingModelForm (forms.ModelForm):
    class Meta:
        model= Toppings
        fields = ['pizza','toppping_name','text']
        #The code below tells Django not to generate a label for the text field.
        labels = {'toppping_name': '','pizza':'','text':'Type in here the description..'}