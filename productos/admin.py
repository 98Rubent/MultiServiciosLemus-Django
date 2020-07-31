from django.contrib import admin

# Register your models here.
from productos.models import Categoria, Producto

class CategoriaAdmin(admin.ModelAdmin):
	list_display = ['nombre']
	search_fields = ['nombre']

class ProductoAdmin(admin.ModelAdmin):
	"""
	search_fields - nos permite habilitar en el admin django
	una barra para buscar segun el criterio que coloquemos Ej. Nombre

	list_display nos despliega en forma de tabla los datos tabulados que
	ya estan guardados en la base de datos
	"""

	list_display = ['pk','nombre' , 'q_precio' , 'garantia']
	search_fields = ['nombre']
	autocomplete_fields=['categoria']

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
