from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, FormView

from apps.revision2.models import Revision2
from apps.revision2.forms import Revision2Form

# Create your views here.

class Revision2List(ListView):
    model = Revision2
    template_name = "revision2/revision2_list.html"

    def get_queryset(self):
        queryset = Revision2.objects.filter(activo=True).order_by('id')
        return queryset


class Revision2Create(CreateView):
    model = Revision2
    form_class = Revision2Form
    template_name = "revision2/revision2_create.html"
    success_url = reverse_lazy("revision2:listar")


class Revision2Update(UpdateView):
    model = Revision2
    form_class = Revision2Form
    template_name = "revision2/revision2_create.html"
    success_url = reverse_lazy("revision2:listar")


class Revision2Delete(DeleteView):
    model = Revision2
    template_name = "revision2/revision2_delete.html"
    success_url = reverse_lazy("revision2:listar")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.activo = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
