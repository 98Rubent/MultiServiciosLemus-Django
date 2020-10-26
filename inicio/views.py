from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from Clientes.models import Cliente
from productos.models import Producto, Categoria, Proveedor
from django.contrib import messages

# Create your views here.
def inicio(request):
    template = loader.get_template('index.html')

    context ={
        '':'',
    }
    return HttpResponse(template.render(context,request))

def home(request):
    template = loader.get_template('home.html')

    context ={
        '':'',
    }
    return HttpResponse(template.render(context,request))

def Conocenos(request):
    template = loader.get_template('conocenos.html')
    context ={
        '':'',
    }
    return HttpResponse(template.render(context,request))

def contacto(request):
    template = loader.get_template('contactanos.html')

    context ={
        '':'',
    }
    return HttpResponse(template.render(context,request))

def log(request):
    template = loader.get_template('login.html')
    context ={
        '':'',
    }
    return HttpResponse(template.render(context,request))

def menuprin(request):
    template = loader.get_template('menu.html')

    context ={
        '':'',
    }
    return HttpResponse(template.render(context,request))

def Boleta(request):
    template = loader.get_template('boleta.html')

    context ={
        '':'',
    }
    return HttpResponse(template.render(context,request))


def Clientes(request):
    #VARIABLES
    datos_a_editar = None
    template = loader.get_template('clientes.html')
    listado_clientes = Cliente.objects.all()

    if request.method == "GET":
        id_vehicle = request.POST.get("id_vehicle", None)

    if request.method == "POST":
        nombres = request.POST.get("nombres", None)
        apellidos = request.POST.get("apellidos", None)
        direccion = request.POST.get("direccion", None)
        nit = request.POST.get("nit", None)
        crear = request.POST.get("crear", None)
        editar = request.POST.get("editar", None)
        id_editar = request.POST.get("id_editar", None)
        editar_datos = request.POST.get("editar_datos", None)
        eliminar = request.POST.get("eliminar", None)
        id_eliminar = request.POST.get("id_eliminar", None)

        print("METODO POST")
        print(editar)
        print(editar_datos)
        print(id_editar)
        if crear:
            print("estoy creando")
            creando = Cliente.objects.create(
                    nombre = nombres,
                    apellidos = apellidos,
                    direccion = direccion,
                    nit = nit
                )
            messages.info(request, "Cliente Creado Exitosamente")

        if editar:
            datos_a_editar = Cliente.objects.get(pk=id_editar)

            if editar_datos:
                datos_a_editar.nombre = nombres
                datos_a_editar.apellidos = apellidos
                datos_a_editar.direccion = direccion
                datos_a_editar.nit = nit
                datos_a_editar.save()
                datos_a_editar = None
                messages.info(request, "Cliente Editado Exitosamente")

        if eliminar:
            Cliente.objects.filter(id=id_eliminar).delete()
            messages.info(request, "Cliente Eliminado Exitosamente")




    context ={
        'listado_clientes':listado_clientes,
        'datos_a_editar': datos_a_editar,
    }
    return HttpResponse(template.render(context,request))


def Productos(request):
    #VARIABLES
    datos_a_editar = None
    template = loader.get_template('productos.html')
    listado_productos = Producto.objects.all()

    if request.method == "GET":
        id_vehicle = request.POST.get("id_vehicle", None)

    if request.method == "POST":
        nombres = request.POST.get("nombres", None)
        precio = request.POST.get("precio", None)
        categoria = request.POST.get("categoria", None)
        proveedor = request.POST.get("proveedor", None)
        garantia = request.POST.get("garantia", None)
        crear = request.POST.get("crear", None)
        editar = request.POST.get("editar", None)
        id_editar = request.POST.get("id_editar", None)
        editar_datos = request.POST.get("editar_datos", None)
        eliminar = request.POST.get("eliminar", None)
        id_eliminar = request.POST.get("id_eliminar", None)

        print("METODO POST")
        print(editar)
        print(editar_datos)
        print(id_editar)
        if crear:
            print("estoy creando")
            creando = Producto.objects.create(

                    nombre = nombres,
                    precio = precio,
                    categoria = categoria,
                    proveedor = proveedor,
                    garantia = garantia,
                )
            messages.info(request, "Producto ingresado Exitosamente")

        if editar:
            datos_a_editar = Producto.objects.get(pk=id_editar)

            if editar_datos:
                datos_a_editar.nombre = nombres
                datos_a_editar.precio = precio
                datos_a_editar.categoria = categoria
                datos_a_editar.proveedor = proveedor
                datos_a_editar.garantia = garantia
                datos_a_editar.save()
                datos_a_editar = None
                messages.info(request, "Producto Editado Exitosamente")

        if eliminar:
            Producto.objects.filter(id=id_eliminar).delete()
            messages.info(request, "Producto Eliminado Exitosamente")



    context ={
            'listado_productos':listado_productos,
            'datos_a_editar': datos_a_editar,
    }
    return HttpResponse(template.render(context,request))



def Categoria(request):
    #VARIABLES
    datos_a_editar = None
    template = loader.get_template('categoria.html')
    listado_categorias = Categoria.objects.all()

    if request.method == "GET":
        id_vehicle = request.POST.get("id_vehicle", None)

    if request.method == "POST":
        nombres = request.POST.get("nombres", None)
        crear = request.POST.get("crear", None)
        editar = request.POST.get("editar", None)
        id_editar = request.POST.get("id_editar", None)
        editar_datos = request.POST.get("editar_datos", None)
        eliminar = request.POST.get("eliminar", None)
        id_eliminar = request.POST.get("id_eliminar", None)

        print("METODO POST")
        print(editar)
        print(editar_datos)
        print(id_editar)
        if crear:
            print("estoy creando")
            creando = Categoria.objects.create(

                    nombre = nombres,

                )
            messages.info(request, "Categoria ingresada Exitosamente")

        if editar:
            datos_a_editar = Categoria.objects.get(pk=id_editar)

            if editar_datos:
                datos_a_editar.nombre = nombres
                datos_a_editar.save()
                datos_a_editar = None
                messages.info(request, "Categoria editada Exitosamente")

        if eliminar:
            Categoria.objects.filter(id=id_eliminar).delete()
            messages.info(request, "Categoria Eliminada Exitosamente")

    context ={
            'listado_categorias':listado_categorias,
            'datos_a_editar': datos_a_editar,
    }
    return HttpResponse(template.render(context,request))


def Proveedores(request):
    template = loader.get_template('proveedores.html')

    context ={
        '':'',
    }
    return HttpResponse(template.render(context,request))



def Reportes(request):
    template = loader.get_template('reportes_devoluciones.html')

    context ={
        '':'',
    }
    return HttpResponse(template.render(context,request))
