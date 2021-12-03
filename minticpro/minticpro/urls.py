"""minticpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from gestionUsuarios import views
from minticpro import views
from minticpro.views import  (ingresar, registrarme)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loguin/', views.ingresar, name='login'),
    path('registrarme/', views.registrarme, name='Registrarme'),

    #Urls de los modulos
    path('', include('gestionUsuarios.urls')),
]