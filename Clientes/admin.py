from django.contrib import admin

from Clientes.models import Cliente
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
	list_display = ['nombre','apellidos','direccion','nit']
	search_fields =['nombre']

admin.site.register(Cliente , ClienteAdmin)