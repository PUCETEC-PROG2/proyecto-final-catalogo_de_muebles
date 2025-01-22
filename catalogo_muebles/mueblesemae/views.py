from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Mueble
from .models import Cliente
# Create your views here.
def index(request):
    muebles = Mueble.objects.all()
    clientes = Cliente.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({
        'muebles': muebles,
        'clientes': clientes
        }, request))

def mueble(request, mueble_id):
    mueble =  Mueble.objects.get(id = mueble_id)
    template = loader.get_template('display_mueble.html')
    context = {
        'mueble': mueble
    }
    return HttpResponse(template.render(context, request))

def cliente_details(request, cliente_id):
    cliente = Cliente.objects.get(id = cliente_id)
    template = loader.get_template('display_cliente.html')
    context = {
        'cliente': cliente
    }
    return HttpResponse(template.render(context, request))
