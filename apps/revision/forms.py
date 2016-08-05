# -*- coding:utf-8 -*-
from django import forms
from apps.registro.models import Registro
from apps.revision.models import Revision


class RevisionForm(forms.ModelForm):

    class Meta:
        model = Revision
        fields = [
            'registro',

            'nombreRevisor1',      
            'observacion1',
            'estado1',

            'nombreRevisor2',      
            'observacion2',
            'estado2',

            'nombreRevisor3',      
            'observacion3',
            'estado3',
        ]
        labels = {
            'registro': 'Folio del oficio:',

            'nombreRevisor1': 'Nombre del 1re revisor:',
            'observacion1': 'Observaciones:',
            'estado1': 'Estado del 1er revisor:',

            'nombreRevisor2': 'Nombre del 2do revisor:',
            'observacion2': '2da observación:',
            'estado2': 'Estado del 2do revisor:',

            'nombreRevisor3': 'Nombre del 3er revisor:',
            'observacion3': '3er observación:',
            'estado3': 'Estado del 3er revisor:',
        }
        widgets = {
            'registro': forms.Select(choices=Registro.objects.all().filter(activo=True).values_list('id'),
                                     attrs={'class': 'form-control'}),

            'nombreRevisor1': forms.TextInput(attrs={'class': 'form-control'}),
            'observacion1': forms.Textarea(attrs={'class': 'form-control'}),
            'estado1': forms.TextInput(attrs={'clas': 'form-control'}),

            'nombreRevisor2': forms.TextInput(attrs={'class': 'form-control'}),
            'observacion2': forms.Textarea(attrs={'class': 'form-control'}),
            'estado2': forms.TextInput(attrs={'clas': 'form-control'}),

            'nombreRevisor3': forms.TextInput(attrs={'class': 'form-control'}),
            'observacion3': forms.Textarea(attrs={'class': 'form-control'}),
            'estado3': forms.TextInput(attrs={'clas': 'form-control'}),

        }