from django.urls import path
#impotamos viewa
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:mueble>", views.get_mueble_details, name="mueble_details")    
]

