from django.contrib import admin

from proveedores.models import Proveedor

# Register your models here.

class ProveedorAdmin(admin.ModelAdmin):
	list_display = ['pk', 'nombre','apellidos','direccion','telefono','nit']
	search_fields = ['nombre','nit']


admin.site.register(Proveedor, ProveedorAdmin)

