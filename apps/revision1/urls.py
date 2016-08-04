from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth.decorators import login_required

from apps.revision1.views import Revision1List, Revision1Create, Revision1Update, Revision1Delete

urlpatterns = [
    url(r'^$', login_required(Revision1List.as_view()), name="listar"),
    url(r'^nuevo$', login_required(Revision1Create.as_view()), name="crear"),
    url(r'^editar/(?P<pk>\d+)$', login_required(Revision1Update.as_view()), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)$', login_required(Revision1Delete.as_view()), name='eliminar'),
]
