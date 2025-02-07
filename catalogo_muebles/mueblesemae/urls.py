from django.urls import path
#impotamos viewa
from . import views
app_name = 'mueblesemae'

urlpatterns = [
    path("", views.index, name="index"),
    path("clientes/", views.clientes, name="clientes"),
    path("cliente_tabla/", views.cliente_tabla, name="cliente_tabla"),
    path("<int:mueble_id>/", views.mueble, name="mueble"),
    path("cliente/<int:cliente_id>/", views.cliente_details, name="cliente_details"),
    path("add_mueble/", views.add_mueble, name="add_mueble"),
    path("edit_mueble/<int:mueble_id>/", views.edit_mueble, name="edit_mueble"),
    path("delete_mueble/<int:mueble_id>/", views.delete_mueble, name="delete_mueble"),
    #clientes
    path("add_cliente/", views.add_cliente, name="add_cliente"),
    path("edit_cliente/<int:cliente_id>/", views.edit_cliente, name="edit_cliente"),
    path("delete_cliente/<int:cliente_id>/", views.delete_cliente, name="delete_cliente"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    
    
]

