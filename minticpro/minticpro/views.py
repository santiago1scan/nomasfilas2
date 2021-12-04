from django.http import HttpResponse
from django.template import Template, context, loader
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .formulario import FormRegistrarme
def ingresar (request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form= AuthenticationForm(request, request.POST)
        if form.is_valid():
            nombreUsuario= form.cleaned_data.get("username")
            contraseña= form.cleaned_data.get("password")
            user = authenticate(username= nombreUsuario, password= contraseña)
            if user is not None:
                #el codigo faltante es de los messages, no estan configurados
                return redirect("hola mundo")#falta hacer la plantilla
    else:
        form= AuthenticationForm()
    return render(request, "login.html", {'formulario': form})

# la funcion registrarme aun no funciona
def registrarme(request):
	if request.method == 'POST':
		form = FormRegistrarme(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			form.save()
			#messages.success(request, 'El usuario %s ha sido creado correctamente.' %username)
	else:
		form = FormRegistrarme()

	params = {'formulario':form}
	return render(request, 'registrarme.html', params)