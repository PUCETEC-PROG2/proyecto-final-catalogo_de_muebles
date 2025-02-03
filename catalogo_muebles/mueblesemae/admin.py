from django.contrib import admin
from .models import Mueble
from .models import Cliente
from .models import Compra
# Register your models here.
@admin.register(Mueble)
class MuebleAdmin(admin.ModelAdmin):
    pass

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    pass
