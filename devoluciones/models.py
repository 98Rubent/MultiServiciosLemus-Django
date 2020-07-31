from django.db import models

from boleta.models import Detalle, Boleta
from django.contrib.auth.models import User

# Create your models here.


"""
este es un modelo que mostrara informacion de la boleta
y la descripcion de una devolucion
"""

class Devolucion(models.Model):

	class Meta:
		verbose_name = 'Tipo de devolución'
		verbose_name_plural = 'Tipos de devoluciones'


	boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
	descripcion=models.TextField('Descripcion')
	usuario = models.ForeignKey(User , on_delete=models.CASCADE)


	#esta funcion devolvera la boleta y su descripcion
	def __str__(self):
		return "{} {}" .format(self.boleta, self.descripcion)


	#esta funcion devolvera el id de la boleta
	def id_boleta(self):
		return "{}".format(self.boleta.pk)
