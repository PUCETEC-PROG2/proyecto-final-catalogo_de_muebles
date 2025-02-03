from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from .models import Mueble
from .models import Cliente
from .models import Compra
from .models import DetalleCompra
from mueblesemae.forms import MuebleForm
from mueblesemae.forms import ClienteForm
from mueblesemae.forms import CompraForm
from mueblesemae.forms import DetalleCompraForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    muebles = Mueble.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({
        'muebles': muebles,
        }, request))



def mueble(request, mueble_id):
    mueble =  Mueble.objects.get(id = mueble_id)
    template = loader.get_template('display_mueble.html')
    context = {
        'mueble': mueble
    }
    return HttpResponse(template.render(context, request))

def clientes(request):    
    clientes = Cliente.objects.all()
    template = loader.get_template('cliente_list.html')
    return HttpResponse(template.render({'clientes': clientes}, request))

#COMPRA
def compra(request):
    compra = Compra.objects.all()
    form = CompraForm()
    template = loader.get_template('compra_form.html')
    return HttpResponse(template.render({'form': form}, request))

def details_compra(request):
    details_compra = DetalleCompra.objects.all()
    form = DetalleCompraForm()
    template = loader.get_template('detalle_compra.html')
    return HttpResponse(template.render({'form': form }, request))

 


#TABLA CLIENTE
def cliente_tabla(request):    
    clientes = Cliente.objects.all()
    template = loader.get_template('cliente_tabla.html')
    return HttpResponse(template.render({'clientes': clientes}, request))

def cliente_details(request, cliente_id):
    cliente = Cliente.objects.get(id = cliente_id)
    template = loader.get_template('display_cliente.html')
    context = {
        'cliente': cliente
    }
    return HttpResponse(template.render(context, request))

#CLIENTE
def add_cliente(request):
    if request.method == "POST": 
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mueblesemae:clientes')
    else:
        form = ClienteForm()        
    return render(request, 'cliente_form.html', {'form': form})

def edit_cliente(request, cliente_id):
    cliente =  Cliente.objects.get(id = cliente_id)
    if request.method == "POST": 
        form = ClienteForm(request.POST, request.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('mueblesemae:clientes')
    else:
        form = ClienteForm(instance=cliente)   
    return render(request, 'cliente_form.html', {'form': form})

def delete_cliente(request, cliente_id):
    cliente =  Cliente.objects.get(id = cliente_id)
    cliente.delete()
    return redirect('mueblesemae:clientes')


#MUEBLE
@login_required
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







#login creado
class CustomLoginView(LoginView):
    template_name = "login_form.html"