from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, FormView

from apps.revision1.models import Revision1
from apps.revision1.forms import Revision1Form

# Create your views here.

class Revision1List(ListView):
    model = Revision1
    paginate_by = 50
    template_name = "revision1/revision1_list.html"

    def get_queryset(self):
        queryset = Revision1.objects.filter(activo=True).order_by('id')
        return queryset


class Revision1Create(CreateView):
    model = Revision1
    form_class = Revision1Form
    template_name = "revision1/revision1_create.html"
    success_url = reverse_lazy("revision1:listar")


class Revision1Update(UpdateView):
    model = Revision1
    form_class = Revision1Form
    template_name = "revision1/revision1_create.html"
    success_url = reverse_lazy("revision1:listar")


class Revision1Delete(DeleteView):
    model = Revision1
    template_name = "revision1/revision1_delete.html"
    success_url = reverse_lazy("revision1:listar")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.activo = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
