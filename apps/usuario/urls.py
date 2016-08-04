from django.conf.urls import url

from apps.usuario.views import RegistroUsuario

from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^registrar', login_required(RegistroUsuario.as_view()), name="registrar")

]