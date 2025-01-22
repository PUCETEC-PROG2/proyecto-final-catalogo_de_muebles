from django.urls import path
#impotamos viewa
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:mueble_id>/", views.mueble, name="mueble"),
    path("cliente/<int:cliente_id>/", views.cliente_details, name="cliente_details")
]

