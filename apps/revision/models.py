from django.db import models

from apps.registro.models import Registro
# Create your models here.

class Revision(models.Model):
	
	registro = models.ForeignKey(Registro)
	
	nombreRevisor1 = models.CharField(max_length=100, null=True, blank=True)
	estado1 = models.CharField(max_length=30, null=True, blank=True)
	observacion1 = models.TextField(max_length=500, null=True, blank=True)

	nombreRevisor2 = models.CharField(max_length=100, null=True, blank=True)
	estado2 = models.CharField(max_length=30, null=True, blank=True)
	observacion2 = models.TextField(max_length=500, null=True, blank=True)
	
	nombreRevisor3 = models.CharField(max_length=100, null=True, blank=True)
	estado3 = models.CharField(max_length=30, null=True, blank=True)
	observacion3 = models.TextField(max_length=500, null=True, blank=True)
	concluido = models.CharField(max_length=30, null=True, blank=True)

	activo = models.BooleanField(default=True)

	def __unicode__(self):
		return u'{} {} {} {}'.format(self.registro, self.estado1, self.estado2, self.estado3)