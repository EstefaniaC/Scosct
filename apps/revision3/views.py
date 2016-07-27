from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, FormView

from apps.revision3.models import Revision3
from apps.revision3.forms import Revision3Form

# Create your views here.

class Revision3List(ListView):
    model = Revision3
    template_name = "revision3/revision3_list.html"

    def get_queryset(self):
        queryset = Revision3.objects.filter(activo=True).order_by('id')
        return queryset


class Revision3Create(CreateView):
    model = Revision3
    form_class = Revision3Form
    template_name = "revision3/revision3_create.html"
    success_url = reverse_lazy("revision3:listar")


class Revision3Update(UpdateView):
    model = Revision3
    form_class = Revision3Form
    template_name = "revision3/revision3_create.html"
    success_url = reverse_lazy("revision3:listar")


class Revision3Delete(DeleteView):
    model = Revision3
    template_name = "revision3/revision3_delete.html"
    success_url = reverse_lazy("revision3:listar")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.activo = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
