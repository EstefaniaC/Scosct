# -*- coding:utf-8 -*-
from django import forms
from apps.registro.models import Registro
from apps.revision3.models import Revision3


class Revision3Form(forms.ModelForm):

    class Meta:
        model = Revision3
        fields = [
            'registro',    
            'nombreRevisor3',      
            'observacion3',
            'estado3',
        ]
        labels = {
            'registro': 'Folio del oficio:',
            'nombreRevisor3': 'Nombre del 3er revisor:',
            'observacion3': 'Observaciones:',
            'estado3': 'Estado del 3er revisor:',
        }
        widgets = {
            'registro': forms.Select(choices=Registro.objects.all().filter(activo=True).values_list('id'),
                                     attrs={'class': 'form-control'}),
            'nombreRevisor3': forms.TextInput(attrs={'class': 'form-control'}),
            'observacion3': forms.Textarea(attrs={'class': 'form-control'}),
            'estado3': forms.TextInput(attrs={'clas': 'form-control'}),
        }