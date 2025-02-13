from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from .models import Mueble
from .models import Cliente
from .models import Compra
from .models import Categoria

from mueblesemae.forms import MuebleForm
from mueblesemae.forms import ClienteForm
from mueblesemae.forms import CompraForm
from mueblesemae.forms import CategoriaForm


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

##MUEBLE-CATEGORIA
def categoria_organizacion(request):
    categorias = Categoria.objects.all()
    template= loader.get_template('mueble_categoria.html')
    return HttpResponse(template.render({
        'categorias': categorias,
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
@login_required
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
        form_categoria = CategoriaForm(request.POST, request.FILES)
        if form.is_valid() and form_categoria.is_valid():
            form.save()
            # form_categoria.save()
            return redirect('mueblesemae:index')
    else:
        form = MuebleForm()  
        form_categoria = CategoriaForm()      
    return render(request, 'mueble_form.html', {'form': form, 'form_categoria': form_categoria})

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


#COMPRA- listado de compra
def listar_compras(request):
    compras = Compra.objects.all().order_by('-fecha')
    template = loader.get_template('lista_compras.html')
    return HttpResponse(template.render({'compras': compras}, request))


#COMPRA- nueva compra
def ingresar_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save()
            compra.calcular_total()
            return redirect('mueblesemae:listar_compras')
    else:
        form = CompraForm()
    
    return render(request, 'ingresar_compra.html', {'form': form})

#COMPRA - DETALLE
def detalle_compra(request, cliente_id, compra_id):
    cliente = Cliente.objects.get(id=cliente_id)
    compra = Compra.objects.get(id=compra_id, cliente=cliente)  # Obtiene solo la compra específica
    return render(request, 'detalle_compra.html', {
        'cliente': cliente,
        'compra': compra,
    })






#login creado
class CustomLoginView(LoginView):
    template_name = "login_form.html"