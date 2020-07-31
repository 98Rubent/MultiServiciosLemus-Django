from django.db import models

# Create your models here.

class Cliente(models.Model):
	
	class Meta:
		verbose_name = 'Cliente'
		verbose_name_plural = 'Clientes'


	"""
	Este modelo guarda la informacion de los clientes
	sus datos principales.
	"""
	
	nombre = models.CharField('Nombres' , max_length=100)
	apellidos = models.CharField('Apellidos' , max_length=100)
	direccion = models.CharField('Direccion' , max_length=150)
	nit = models.CharField('NIT' , max_length=12 , default="C/F", blank = True, null= True)

	"""
	Esto es una funcion de python que permite devolver
	los  valores que guarda,para visualizarlos en el admin
	"""
	
	def __str__(self):
		return "{} {} ".format(self.nombre, self.apellidos)