from django.contrib import admin
from .models import Mueble
# Register your models here.
@admin.register(Mueble)
class MuebleAdmin(admin.ModelAdmin):
    pass