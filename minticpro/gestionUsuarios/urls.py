from django.urls import path
from gestionUsuarios import views
from gestionUsuarios.views import  (PaginaPrincipal)

urlpatterns = [
	path('PaginaPrincipal/', views.PaginaPrincipal, name='PaginaPrincipal'),
	
]
