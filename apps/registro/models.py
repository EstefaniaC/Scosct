from django.db import models

# Create your models here.

class Registro(models.Model):
	
    nombreEntrega = models.CharField(max_length=50,null=True, blank=True)
    numeroFolio = models.IntegerField(null=True, blank=True)
    asunto = models.CharField(max_length=50,null=True, blank=True)
    numeroOficio = models.CharField(max_length=50,null=True, blank=True)
    coordinador = models.CharField(max_length=50,null=True, blank=True)
    empresa = models.CharField(max_length=50,null=True, blank=True)
    fechaRecibido = models.DateField()
    modalidad =models.CharField(max_length=50,null=True, blank=True)
    fechaEntrega = models.DateField()
    municipio = models.CharField(max_length=25,null=True, blank=True)
    observacion = models.TextField(max_length=500)
    activo = models.BooleanField(default=True)
    
    def __unicode__(self):
        return u'{}'.format(self.numeroOficio)