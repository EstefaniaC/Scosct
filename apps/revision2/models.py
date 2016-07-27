from django.db import models

from apps.registro.models import Registro
# Create your models here.

class Revision2(models.Model):
	
	registro = models.ForeignKey(Registro)
	nombreRevisor2 = models.CharField(max_length=100, null=True, blank=True)
	estado2 = models.CharField(max_length=30, null=True, blank=True)
	observacion2 = models.TextField(max_length=500, null=True, blank=True)
	activo = models.BooleanField(default=True)

	def __unicode__(self):
		return u'{}'.format(self.nombreRevisor2)
