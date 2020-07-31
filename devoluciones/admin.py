from django.contrib import admin

# Register your models here.

"""
importamos las apps de devoluciones y boleta para
poder mostrar el id de boleta, los datos del cliente
contenidos en la boleta y su descripcion
"""
from devoluciones.models import Devolucion
from boleta.models import Detalle, Boleta

class DevolucionAdmin(admin.ModelAdmin):
	list_display = ['pk', 'usuario', 'boleta','descripcion']
	search_fields = ['boleta']
	autocomplete_fields = ['boleta']
	list_filter = ['usuario']


admin.site.register(Devolucion, DevolucionAdmin)
