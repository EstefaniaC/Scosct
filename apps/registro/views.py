from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, FormView

from apps.registro.models import Registro
from apps.registro.forms import RegistroForm

# Create your views here.

class RegistroList(ListView):
    model = Registro
    template_name = "registro/registro_list.html"

    def get_queryset(self):
        queryset = Registro.objects.filter(activo=True).order_by('id')
        return queryset


class RegistroCreate(CreateView):
    model = Registro
    form_class = RegistroForm
    template_name = "registro/registro_create.html"
    success_url = reverse_lazy("registro:listar")


class RegistroUpdate(UpdateView):
    model = Registro
    form_class = RegistroForm
    template_name = "registro/registro_create.html"
    success_url = reverse_lazy("registro:listar")


class RegistroDelete(DeleteView):
    model = Registro
    template_name = "registro/registro_delete.html"
    success_url = reverse_lazy("registro:listar")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.activo = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
