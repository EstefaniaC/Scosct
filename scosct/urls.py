"""scosct URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

#from scosct.views import Index
from django.contrib.auth.views import login


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	#url(r'^$', Index.as_view(), name="index"),
    url(r'^inicio/', include('apps.administrador.urls', namespace="administrador")),
    url(r'^registro/', include('apps.registro.urls', namespace="registro")),
    url(r'^revision1/', include('apps.revision1.urls', namespace="revision1")),
    url(r'^revision2/', include('apps.revision2.urls', namespace="revision2")),
    url(r'^revision3/', include('apps.revision3.urls', namespace="revision3")),   
    url(r'^usuario/', include('apps.usuario.urls', namespace="usuario")),   
    url(r'^login', login, {'template_name':'index.html'}, name='login'),
]
