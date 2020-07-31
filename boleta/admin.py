from django.contrib import admin

# Register your models here.
from Clientes.models import Cliente
from productos.models import Categoria, Producto
from boleta.models import Detalle, Boleta

"""
importamos clientes, productos y  boleta
"""


class dataClientes(admin.TabularInline):
	model= Cliente
	extra = 1
	max_num = 3

"""

"""

class BoletaDetalle(admin.TabularInline):
	model = Detalle
	extra = 0
	min_num = 1
	max_num = 15

class DetalleAdmin(admin.ModelAdmin):
	list_display = ['pk','fecha', 'boleta', 'cantidad' , 'producto','calcular_total'] # mostrar el detalle de la venta con pk,boleta,cantidad y prod
	search_fields = ['pk','boleta'] # buscar por pk y boleta
	autocomplete_fields = ['producto'] # autocompletar con la boleta


class BoletaAdmin(admin.ModelAdmin):
#	inlines = [dataClientes]
	inlines = [BoletaDetalle]
	list_display = ['pk', 'cliente','direccion' ,'fecha','calcular_total' , 'imprimir'] #listar la boleta con pk,cliente,fecha,estado
	search_fields = ['pk','cliente', 'fecha'] #buscar con pk,cliente y fecha
	autocomplete_fields= ['cliente', 'usuario'] #autocompletar con la pk,cliente y fecha




# admin.site.register(Detalle , DetalleAdmin)
admin.site.register(Boleta , BoletaAdmin)
