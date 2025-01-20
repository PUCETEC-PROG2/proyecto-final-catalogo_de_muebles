from django.urls import path
#impotamos viewa
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:mueble_id>/", views.mueble, name="mueble")    
]

