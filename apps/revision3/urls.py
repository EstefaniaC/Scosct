from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth.decorators import login_required

from apps.revision3.views import Revision3List, Revision3Create, Revision3Update, Revision3Delete

urlpatterns = [
    url(r'^$', login_required(Revision3List.as_view()), name="listar"),
    url(r'^nuevo$', login_required(Revision3Create.as_view()), name="crear"),
    url(r'^editar/(?P<pk>\d+)$', login_required(Revision3Update.as_view()), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)$', login_required(Revision3Delete.as_view()), name='eliminar'),
]
