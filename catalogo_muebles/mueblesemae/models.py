from django.db import models
#from .models import Mueble

# Create your models here.
class Mueble(models.Model):
    
    # MUEBLE_NAME ={
    #     ('Armario', 'Armario'),
    #     ('Sala de Estar', 'Sala de Estar'),
    #     ('Cama', 'Cama'),
    # }
    name = models.CharField(max_length=15, null=False)
    MUEBLE_TYPES = {
        ('A', 'Organizacion'),
        ('H', 'Hool/Entrada'),
        ('B', 'Confort'),
    }
    type = models.CharField(max_length=30, choices=MUEBLE_TYPES, null=False)
    MUEBLE_MATERIALS = {
        ('M', 'Madera Sostenible'),
        ('B', 'Bambu'),
        ('E', 'Eco-plasticos'),
        ('C', 'Corcho'),
        ('LO', 'Lino Orgonico'),
        ('FC', 'Fibras de Coco'),    
    }
    materials = models.CharField(max_length=30, choices=MUEBLE_MATERIALS, null=False)
    MUEBLE_STYLES = {
        ('M', 'Minimalista'),
        ('MU', 'Multifuncionales'),
        ('S', 'Sostenibles'),
        ('I', 'Industrial'),
    }
    styles = models.CharField(max_length=30, choices=MUEBLE_STYLES, null=False)
    
    def __str__(self):
        return self.name
    
    