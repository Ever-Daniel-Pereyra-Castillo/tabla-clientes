from django.shortcuts import render, redirect
from .models import Sucursales
# Create your views here.
def inicio_vistaSucursal(request):
    lasSucursales=Sucursales.objects.all()
    return render(request,"gestionarSucursales.html", {"misSucursales":lasSucursales}   )

def registrarSucursales(request):
    ID_Sucursal=request.POST["numID_Sucursal"]
    Nombre=request.POST["txtNombre"]
    Direccion=request.POST["txtDireccion"]
    Horario=request.POST["txtHorario"]
    Encargado=request.POST["txtEncargado"]
    Correo=request.POST["txtCorreo"]
    Telefono=request.POST["numTelefono"]
    
    guardarSucursales=Sucursales.objects.create(
        ID_Sucursal=ID_Sucursal,Nombre=Nombre,Direccion=Direccion,Horario=Horario,Encargado=Encargado,Correo=Correo,Telefono=Telefono
    ) #GUARDA EL REGISTRO
    
    return redirect("sucursales")

def seleccionarSucursales(request,ID_Sucursal):
    sucursales=Sucursales.objects.get(ID_Sucursal=ID_Sucursal)
    return render(request, "editarSucursales.html",{"misSucursales":sucursales})

def editarSucursales(request):
    ID_Sucursal=request.POST["numID_Sucursal"]
    Nombre=request.POST["txtNombre"]
    Direccion=request.POST["txtDireccion"]
    Horario=request.POST["txtHorario"]
    Encargado=request.POST["txtEncargado"]
    Correo=request.POST["txtCorreo"]
    Telefono=request.POST["numTelefono"]
    sucursales=Sucursales.objects.get(ID_Sucursal=ID_Sucursal)
    sucursales.Nombre=Nombre
    sucursales.Direccion=Direccion
    sucursales.Horario=Horario
    sucursales.Encargado=Encargado
    sucursales.Correo=Correo
    sucursales.Telefono=Telefono
    
    sucursales.save() #guarda registro actualizado
    return redirect("sucursales")

def borrarSucursales(request,ID_Sucursal):
    sucursales=Sucursales.objects.get(ID_Sucursal=ID_Sucursal)
    sucursales.delete() # borra el registro
    return redirect("sucursales")