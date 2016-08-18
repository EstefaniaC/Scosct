# -*- coding:utf-8 -*-
from django import forms

from apps.registro.models import Registro


class RegistroForm(forms.ModelForm):

    class Meta:
        model = Registro
        fields = [
            'nombreEntrega',
            'numeroOficio',
            'asunto',
            'coordinador',
            'empresa',
            'fechaRecibido',
            'modalidad',
            'fechaEntrega',
            'municipio',
            'observacion',
            'oficio',
        ]
        labels = {
            'nombreEntrega': 'Nombre del solicitante:',
            'numeroOficio': 'Folio del oficio:',
            'asunto': 'Asunto:',
            'coordinador': 'Coordinador:',
            'empresa': 'Empresa:',
            'fechaRecibido': 'Fecha de recibido:',
            'modalidad': 'Modalidad:',
            'fechaEntrega': 'Fecha de entrega:',
            'municipio': 'Municipio:',
            'observacion': 'Observaciones:',
            'oficio': 'Oficio inicial:',
        }
        widgets = {
            'nombreEntrega': forms.TextInput(attrs={'class': 'form-control'}),
            'numeroOficio': forms.TextInput(attrs={'class': 'form-control'}),
            'asunto': forms.TextInput(attrs={'class': 'form-control'}),
            'coordinador': forms.TextInput(attrs={'class': 'form-control'}),
            'empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaRecibido': forms.DateInput(attrs={'class': 'js-datepicker form-control',
                                                                'data-date-format': 'yyyy-mm-dd'}),
            'modalidad': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaEntrega': forms.DateInput(attrs={'class': 'js-datepicker form-control',
                                                                'data-date-format': 'yyyy-mm-dd'}),
            'municipio': forms.TextInput(attrs={'class': 'form-control'}),
            'observacion': forms.Textarea(attrs={'class': 'form-control'}),
        }