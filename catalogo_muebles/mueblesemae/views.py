from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Mueble

# Create your views here.
def index(request):
    muebles = Mueble.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'muebles':muebles}, request))

def mueble(request, mueble_id):
    mueble =  Mueble.objects.get(id = mueble_id)
    template = loader.get_template('display_mueble.html')
    context = {
        'mueble': mueble
    }
    return HttpResponse(template.render(context, request))

# def get_mueble_details(request, mueble):
#     template = loader.get_template('mueble_details.html')
#     return HttpResponse(template.render({'mueble':mueble}, request)) 
