from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth.decorators import login_required

from apps.revision.views import RevisionList, Revision2List, BuscarView, RevisionCreate, RevisionUpdate, Revision2Update, Revision3Update, RevisionDelete

urlpatterns = [
    url(r'^$', login_required(RevisionList.as_view()), name="listar"),
    url(r'^nuevo$', login_required(RevisionCreate.as_view()), name="crear"),
    url(r'^revisor1/(?P<pk>\d+)$', login_required(RevisionUpdate.as_view()), name='revisor1'),
    url(r'^eliminar/(?P<pk>\d+)$', login_required(RevisionDelete.as_view()), name='eliminar'),
    url(r'^revisor2/(?P<pk>\d+)$', login_required(Revision2Update.as_view()), name='revisor2'),
    url(r'^revisor3/(?P<pk>\d+)$', login_required(Revision3Update.as_view()), name='revisor3'),
    url(r'^consulta', login_required(Revision2List.as_view()), name="consulta"),

    url(r'^buscar', login_required(BuscarView.as_view()), name="buscar"),

]
