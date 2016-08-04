from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth.decorators import login_required

from apps.revision2.views import Revision2List, Revision2Create, Revision2Update, Revision2Delete

urlpatterns = [
    url(r'^$', login_required(Revision2List.as_view()), name="listar"),
    url(r'^nuevo$', login_required(Revision2Create.as_view()), name="crear"),
    url(r'^editar/(?P<pk>\d+)$', login_required(Revision2Update.as_view()), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)$', login_required(Revision2Delete.as_view()), name='eliminar'),
]
