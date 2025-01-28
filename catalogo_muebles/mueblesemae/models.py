from django.db import models
from django.db.models import  Q

# Create your models here.

##MUEBLES
class Tipo_mueble(models.Model):
    type_furniture = models.CharField(max_length=30, null=False)
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(type_furniture__in=['Organizacion', 'Hool', 'Confort']),
                name='check_types_furniture'
            ),
        ]
        
    def __str__(self):
        return self.type_furniture
    
class Mueble(models.Model):
    name = models.CharField(max_length=15, null=False)
    MUEBLE_MATERIALS = (
        ('M', 'Madera Sostenible'),
        ('B', 'Bambu'),
        ('E', 'Eco-plasticos'),
        ('C', 'Corcho'),
        ('L', 'Lino Orgonico'),
        ('F', 'Fibras de Coco'),    
    )
    material = models.CharField(max_length=30, null=False, choices=MUEBLE_MATERIALS)
    MUEBLE_STYLES = (
        ('M', 'Minimalista'),
        ('M', 'Multifuncionales'),
        ('S', 'Sostenibles'),
        ('I', 'Industrial'),
    )
    style = models.CharField(max_length=30, null=False, choices=MUEBLE_STYLES)
    cost = models.DecimalField(decimal_places = 4, max_digits = 6, null=False, default=0)
    
    picture = models.ImageField(upload_to="muebles_images")
    type = models.ForeignKey(Tipo_mueble, on_delete=models.CASCADE)
    
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
    
