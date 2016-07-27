from django.conf.urls import include, url
from django.contrib import admin

from apps.revision3.views import Revision3List, Revision3Create, Revision3Update, Revision3Delete

urlpatterns = [
    url(r'^$', Revision3List.as_view(), name="listar"),
    url(r'^nuevo$', Revision3Create.as_view(), name="crear"),
    url(r'^editar/(?P<pk>\d+)$', Revision3Update.as_view(), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)$', Revision3Delete.as_view(), name='eliminar'),
]
