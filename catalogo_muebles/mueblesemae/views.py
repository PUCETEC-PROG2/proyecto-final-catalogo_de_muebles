from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    muebles = ['Armario', 'Escritorio', 'Cama', 'Silla']
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'muebles':muebles}, request))

def get_mueble_details(request, mueble):
    template = loader.get_template('mueble_details.html')
    return HttpResponse(template.render({'mueble':mueble}, request))
