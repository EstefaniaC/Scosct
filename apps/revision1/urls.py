from django.conf.urls import include, url
from django.contrib import admin

from apps.revision1.views import Revision1List, Revision1Create, Revision1Update, Revision1Delete

urlpatterns = [
    url(r'^$', Revision1List.as_view(), name="listar"),
    url(r'^nuevo$', Revision1Create.as_view(), name="crear"),
    url(r'^editar/(?P<pk>\d+)$', Revision1Update.as_view(), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)$', Revision1Delete.as_view(), name='eliminar'),
]
