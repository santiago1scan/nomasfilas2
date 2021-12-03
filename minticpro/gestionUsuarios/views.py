from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, context, loader


# Create your views here.

def PaginaPrincipal(request):
    pass
    return render(request, "PaginaPrincipal.html")