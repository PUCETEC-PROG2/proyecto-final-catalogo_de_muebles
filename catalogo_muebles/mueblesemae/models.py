from django.db import models


# Create your models here.



##MUEBLES
class Mueble(models.Model):
    
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

class Cliente(models.Model):
    name = models.CharField(max_length=15, null=False)
    last_name = models.CharField(max_length=15, null=False)
    dni = models.IntegerField(null=False, unique=True)
    email = models.EmailField(max_length=50, null=True)
    furniture = models.ForeignKey(Mueble, on_delete=models.RESTRICT)
    
    def __str__(self):
        return self.name + " " + self.last_name