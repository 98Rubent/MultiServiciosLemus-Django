"""Ventas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from inicio.views import inicio, home, Conocenos, contacto, log, menuprin, POS, Clientes, Productos, Categoria_CRUD, Proveedores_CRUD, Reportes
from boleta.views import Printer

# import from user views
from usuarios.views import LoginView , LogoutView

#from django.urls import path, include
#from django.contrib.auth.models import User
#from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
#class UserSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = User
#        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
#class UserViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
#router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', home , name="index"),
    path('login/' , LoginView.as_view() , name="login"),
    path('login/' , LogoutView.as_view() , name="logout"),
    path('index/', inicio),
    path('conocenos/', Conocenos , name="conocenos"),
    path('contactanos/', contacto , name="contactanos"),
    # path('login/', log , name="login"),
    path('menu/', menuprin , name="menu"),
    path('POS/', POS, name="pos"),
    path('clientes/', Clientes , name="clientes"),
    path('productos/', Productos , name="productos"),
    path('categoria/', Categoria_CRUD, name="categorias"),
    path('proveedores/', Proveedores_CRUD, name="proveedores"),
    path('reportes_devoluciones/', Reportes, name="reports"),

#    path('', include(router.urls)),
#    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    url(r"^imprimir/(?P<id>)", Printer.as_view()),
]
