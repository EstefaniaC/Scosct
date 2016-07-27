from django.conf.urls import include, url
from django.contrib import admin

from apps.revision2.views import Revision2List, Revision2Create, Revision2Update, Revision2Delete

urlpatterns = [
    url(r'^$', Revision2List.as_view(), name="listar"),
    url(r'^nuevo$', Revision2Create.as_view(), name="crear"),
    url(r'^editar/(?P<pk>\d+)$', Revision2Update.as_view(), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)$', Revision2Delete.as_view(), name='eliminar'),
]
