# -*- coding:utf-8 -*-
from django import forms

from apps.registro.models import Registro


class RegistroForm(forms.ModelForm):

    class Meta:
        model = Registro
        fields = [
            'nombreEntrega',
            'numeroFolio',
            'asunto',
            'numeroOficio',
            'coordinador',
            'empresa',
            'fechaRecibido',
            'modalidad',
            'fechaEntrega',
            'municipio',
            'observacion',
        ]
        labels = {
            'nombreEntrega': 'Nombre de quien entrega el Oficio:',
            'numeroFolio': 'Número de registro:',
            'asunto': 'Asunto:',
            'numeroOficio': 'Número de oficio del oficio:',
            'coordinador': 'Coordinador:',
            'empresa': 'Empresa',
            'fechaRecibido': 'Fecha de recibido:',
            'modalidad': 'Modalidad:',
            'fechaEntrega': 'Fecha de entrega:',
            'municipio': 'Municipio:',
            'observacion': 'Observaciones:',
        }
        widgets = {
            'nombreEntrega': forms.TextInput(attrs={'class': 'form-control'}),
            'numeroFolio': forms.TextInput(attrs={'class': 'form-control'}),
            'asunto': forms.TextInput(attrs={'class': 'form-control'}),
            'numeroOficio': forms.TextInput(attrs={'class': 'form-control'}),
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