from django.urls import path
#impotamos viewa
from . import views
app_name = 'mueblesemae'

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:mueble_id>/", views.mueble, name="mueble"),
    path("cliente/<int:cliente_id>/", views.cliente_details, name="cliente_details"),
    path("add_mueble/", views.add_mueble, name="add_mueble"),
    path("edit_mueble/<int:mueble_id>/", views.edit_mueble, name="edit_mueble"),
    path("delete_mueble/<int:mueble_id>/", views.delete_mueble, name="delete_mueble"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    
    
    
]

