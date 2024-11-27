from django.urls import path
from sucursal_app import views
urlpatterns = [
    path("sucursales", views.inicio_vistaSucursal, name= "sucursales" ),
    path("registrarSucursales/",views.registrarSucursales,name="registrarSucursales"),
    path("seleccionarSucursales/<ID_Sucursal>",views.seleccionarSucursales,name="seleccionarSucursales"),
    path("editarSucursales/",views.editarSucursales,name="editarSucursales"),
    path("borrarSucursales/<ID_Sucursal>",views.borrarSucursales,name="borrarSucursales")
]
