from django.conf.urls import include, url
from django.contrib import admin

from apps.administrador.views import Inicio

urlpatterns = [
    url(r'^$', Inicio.as_view(), name="inicio"),
]