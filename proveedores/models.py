from django.db import models

# Create your models here.



class Proveedor(models.Model):
	
	class Meta:
		verbose_name = 'Proveedor'
		verbose_name_plural = 'Proveedores'

	
	"""
	este modelo contiene la informacion de los 
	proveedores con sus datos principales
	"""

	nombre = models.CharField('Nombres' , max_length=100)
	apellidos = models.CharField('Apellidos' , max_length=100)
	direccion = models.CharField('Direccion' , max_length=150)
	telefono = models.CharField('Telefono', max_length=8)
	nit = models.CharField('NIT' , max_length=12 , default="C/F", blank = True, null= True)

	"""
	esto es una funcion de python que permite devolver
	los datos guardados y luego visualizarlos en el admin
	"""

	def __str__(self):
		return "{} {} -NIT:{}".format(self.nombre, self.apellidos, self.nit)


