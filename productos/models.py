from django.db import models

from proveedores.models import Proveedor
# Create your models here.


class Categoria(models.Model):

	nombre = models.CharField('Nombre' , max_length=50)


	class Meta:
		verbose_name = 'Tipo de categoria'
		verbose_name_plural = 'Tipos de categorias'

	"""
	Este modelo nos sirve para almacenar las categorias
	para poder hacer relacion con los productos
	ForeignKey == llave de uno a muchos
	"""


	def __str__(self):
		return " {}".format(self.nombre)



class Producto(models.Model):

	class Meta:
		verbose_name = 'Tipo de producto'
		verbose_name_plural = 'Tipos de productos'

	"""
	Este modelo almacena la informacion de los productos
	tiene una relacion con categoria
	el precio tiene 7 posiciones ej 99 999.00
	y dos decimales
	"""

	nombre = models.CharField("Nombre" , max_length =50)
	precio = models.DecimalField("Precio" , default=0, decimal_places=2, max_digits=7)
	categoria = models.ForeignKey(Categoria , on_delete=models.CASCADE)
	proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
	garantia = models.CharField("Garantia", max_length=50)


	"""
	esta funcion devuelve en el admin los datos del producto
	"""

	def __str__(self):
		return "{} - Q.{}".format(self.nombre, self.precio)

	def q_precio(self):
		return "Q.{} ".format(self.precio)
