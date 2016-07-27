# -*- coding:utf-8 -*-
from django import forms
from apps.registro.models import Registro
from apps.revision1.models import Revision1


class Revision1Form(forms.ModelForm):

    class Meta:
        model = Revision1
        fields = [
            'registro',      
            'nombreRevisor1',      
            'observacion_1',
            'estado',
        ]
        labels = {
            'registro': 'Folio del oficio:',
            'nombreRevisor1': 'Nombre del 1re revisor:',
            'observacion_1': 'Observaciones:',
            'estado': 'Estado del 1er revisor:',
        }
        widgets = {
            'registro': forms.Select(choices=Registro.objects.all().filter(activo=True).values_list('id'),
                                     attrs={'class': 'form-control'}),
            'nombreRevisor1': forms.TextInput(attrs={'class': 'form-control'}),
            'observacion_1': forms.Textarea(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'clas': 'form-control'}),
        }