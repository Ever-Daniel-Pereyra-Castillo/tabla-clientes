from django.shortcuts import render, redirect
from .models import Sucursales
# Create your views here.
def inicio_vista(request):
    lasSucursales=Sucursales.objects.all()
    return render(request,"gestionarSucursales.html", {"misSucursales":lasSucursales}   )

def registrarSucursales(request):
    ID_sucursal=request.POST["numID_sucursal"]
    Nombre=request.POST["txtNombre"]
    Direccion=request.POST["txtDireccion"]
    Horario=request.POST["txtHorario"]
    Encargado=request.POST["txtEncargado"]
    Correo=request.POST["txtCorreo"]
    Telefono=request.POST["numSaldo"]
    
    guardarSucursales=Sucursales.objects.create(
        ID_sucursal=ID_sucursal,Nombre=Nombre,Direccion=Direccion,Horario=Horario,Encargado=Encargado,Correo=Correo,Telefono=Telefono
    ) #GUARDA EL REGISTRO
    
    return redirect("/")

def seleccionarSucursales(request,ID_sucursal):
    sucursales=Sucursales.objects.get(ID_sucursal=ID_sucursal)
    return render(request, "editarSucursales.html",{"misSucursales":sucursales})

def editarSucursales(request):
    ID_sucursal=request.POST["numID_sucursal"]
    Nombre=request.POST["txtNombre"]
    Direccion=request.POST["txtDireccion"]
    Horario=request.POST["txtHorario"]
    Encargado=request.POST["txtEncargado"]
    Correo=request.POST["txtCorreo"]
    Telefono=request.POST["numSaldo"]
    sucursales=Sucursales.objects.get(ID_sucursal=ID_sucursal)
    sucursales.Nombre=Nombre
    sucursales.Direccion=Direccion
    sucursales.Horario=Horario
    sucursales.Encargado=Encargado
    sucursales.Correo=Correo
    sucursales.Telefono=Telefono
    
    sucursales.save() #guarda registro actualizado
    return redirect("/")

def borrarSucursales(request,ID_sucursal):
    sucursales=Sucursales.objects.get(ID_sucursal=ID_sucursal)
    sucursales.delete() # borra el registro
    return redirect("/")