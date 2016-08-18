from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth.decorators import login_required

from apps.registro.views import RegistroList, RegistroCreate, RegistroUpdate,\
								RegistroDelete, RegistroVisualizar

urlpatterns = [
    url(r'^$', login_required(RegistroList.as_view()), name="listar"),
    url(r'^nuevo$', login_required(RegistroCreate.as_view()), name="crear"),
    url(r'^editar/(?P<pk>\d+)$', login_required(RegistroUpdate.as_view()), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)$', login_required(RegistroDelete.as_view()), name='eliminar'),
    url(r'^visualizar/(?P<pk>\d+)$', login_required(RegistroVisualizar.as_view()), name='visualizar'),
]
