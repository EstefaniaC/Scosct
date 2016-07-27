# -*- coding:utf-8 -*-
from django import forms
from apps.registro.models import Registro
from apps.revision2.models import Revision2


class Revision2Form(forms.ModelForm):

    class Meta:
        model = Revision2
        fields = [
            'registro',    
            'nombreRevisor2',      
            'observacion2',
            'estado2',
        ]
        labels = {
            'registro': 'Folio del oficio:',
            'nombreRevisor2': 'Nombre del 2do revisor:',
            'observacion2': 'Observaciones:',
            'estado2': 'Estado del 2do revisor:',
        }
        widgets = {
            'registro': forms.Select(choices=Registro.objects.all().filter(activo=True).values_list('id'),
                                     attrs={'class': 'form-control'}),
            'nombreRevisor2': forms.TextInput(attrs={'class': 'form-control'}),
            'observacion2': forms.Textarea(attrs={'class': 'form-control'}),
            'estado2': forms.TextInput(attrs={'clas': 'form-control'}),
        }