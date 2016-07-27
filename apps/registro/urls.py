from django.conf.urls import include, url
from django.contrib import admin

from apps.registro.views import RegistroList, RegistroCreate, RegistroUpdate, RegistroDelete

urlpatterns = [
    url(r'^$', RegistroList.as_view(), name="listar"),
    url(r'^nuevo$', RegistroCreate.as_view(), name="crear"),
    url(r'^editar/(?P<pk>\d+)$', RegistroUpdate.as_view(), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)$', RegistroDelete.as_view(), name='eliminar'),
]
