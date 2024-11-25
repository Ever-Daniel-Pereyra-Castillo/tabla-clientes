from django.urls import path
from clientes_app import views
urlpatterns = [
    path("clientes", views.inicio_vistaClientes, name= "clientes" ),
    path("registrarClientes/",views.registrarClientes,name="registrarClientes"),
    path("seleccionarClientes/<ID_cliente>",views.seleccionarClientes,name="seleccionarClientes"),
    path("editarClientes/",views.editarClientes,name="editarClientes"),
    path("borrarClientes/<ID_cliente>",views.borrarClientes,name="borrarClientes"),
]
