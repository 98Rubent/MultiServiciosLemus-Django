from django.shortcuts import render

from django.contrib.auth import views as auth_views

# Create your views here.



class LoginView(auth_views.LoginView):
    template_name = 'login.html'
    success_message = "Bienvenido!"


class LogoutView(auth_views.LogoutView):
    pass
    # template_name = 'productos/logged_out.html'
