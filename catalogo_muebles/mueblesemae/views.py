from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from .models import Mueble
from .models import Cliente
from mueblesemae.forms import MuebleForm

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

def add_mueble(request):
    if request.method == "POST": 
        form = MuebleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mueblesemae:index')
    else:
        form = MuebleForm()        
    return render(request, 'mueble_form.html', {'form': form})

def edit_mueble(request, mueble_id):
    mueble =  Mueble.objects.get(id = mueble_id)
    if request.method == "POST": 
        form = MuebleForm(request.POST, request.FILES, instance=mueble)
        if form.is_valid():
            form.save()
            return redirect('mueblesemae:index')
    else:
        form = MuebleForm(instance=mueble)   
    return render(request, 'mueble_form.html', {'form': form})

def delete_mueble(request, mueble_id):
    mueble =  Mueble.objects.get(id = mueble_id)
    mueble.delete()
    return redirect('mueblesemae:index')    