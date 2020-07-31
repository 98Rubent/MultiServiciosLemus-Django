from django.db import models
from django.utils.safestring import mark_safe

#IMPORTAMOS EL MODULO DE USUARIOS DE DJANGO
from django.contrib.auth.models import User

from Clientes.models import Cliente
from productos.models import Producto
# Create your models here.

"""
NOTA: PARA USAR LA RELACION ENTRE EL USUARIO QUE TRAE django
es necesario hacer el import ddel modelo
from django.contrib.auth.models import User
y hacer la foranea en el modelo que necesitemos
"""


class Boleta(models.Model):

	"""
	class Meta: nos permite mostrar los nombres de nuestras apps en el framework con el nombre
	que debemos darle tambien evita que se le agreguen los guiones bajos en caso si se tuvieran
	espacios
	"""
	class Meta:
		verbose_name = 'Boleta'
		verbose_name_plural = 'Boletas'

	"""
	Este modelo guardara todos los datos
	referentes a la venta que se realizará
	de los productos
	"""

	fecha = models.DateField('Fecha', auto_now_add=True)#el sistema captura la fecha en el momento exacto
	estado = models.BooleanField('Estado', default=True)
	cliente = models.ForeignKey(Cliente , on_delete=models.CASCADE)
	usuario = models.ForeignKey(User , on_delete=models.CASCADE)

	"""
	CASCADE: si tengo grupo de registros del mismo cliente y si se desea
	borrar sus registros CASCADE eliminara todos sus registros del cliente

	esto es una funcion de python que permite devolver
	los valores que guarda para visualizarlos en el admin
	"""


	def __str__(self):
		return "{}".format(self.cliente)

	def imprimir(self):
		return mark_safe(
		u'<a href="/imprimir/?id=%s" target="_blank" class="addlink">IMPRIMIR</a>'% self.id
		)
		ficha.short_description = 'IMPRIMIR'


	"""
	funcion para devolver la direccion del cliente
	"""

	def direccion(self):
		return "{}".format(self.cliente.direccion)

	#calcular total	de venta

	def calcular_total(self):
		id_venta=self.pk
		articulos=Detalle.objects.filter(boleta=id_venta)
		total=0
		for articulo in articulos:
			subtotal=articulo.cantidad * articulo.producto.precio #  cantidad * producto = total
			total += subtotal

		return "Q.{}".format(total) # devolvemos el total de la venta





class Detalle(models.Model):

	class Meta:
		verbose_name = 'Detalle de venta'
		verbose_name_plural = 'Detalles de ventas'

	"""
	Este modelo guardara el detalle de la venta
	"""
	cantidad = models.PositiveIntegerField('Cantidad', help_text='Ingresar solo numeros positivos.')
	boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

	"""
	esto es una funcion de python que permite devolver
	los valores que guarda para visualizarlos en el admin
	"""

	def __str__(self):
		return "{} {} {}".format(self.boleta.pk, self.cantidad, self.producto)

	"""
	funcion que devuelte la fecha en que se crea la boleta
	"""

	def fecha(self):
		return "{}".format(self.boleta.fecha)
