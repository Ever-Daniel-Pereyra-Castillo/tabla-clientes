from django.shortcuts import render, redirect
from .models import Clientes
# Create your views here.
def inicio_vista(request):
    losClientes=Clientes.objects.all()
    return render(request,"gestionarClientes.html", {"misClientes":losClientes}   )

def registrarClientes(request):
    ID_cliente=request.POST["numID_cliente"]
    Nombre=request.POST["txtNombre"]
    Correo=request.POST["txtCorreo"]
    Forma_de_pago=request.POST["txtForma_de_pago"]
    Productos=request.POST["txtProductos"]
    Saldo=request.POST["numSaldo"]
    Direccion=request.POST["txtDireccion"]
    
    guardarClientes=Clientes.objects.create(
        ID_cliente=ID_cliente,Nombre=Nombre,Correo=Correo,Forma_de_pago=Forma_de_pago,Productos=Productos,Saldo=Saldo,Direccion=Direccion
    ) #GUARDA EL REGISTRO
    
    return redirect("/")

def seleccionarClientes(request,ID_cliente):
    clientes=Clientes.objects.get(ID_cliente=ID_cliente)
    return render(request, "editarClientes.html",{"misClientes":clientes})

def editarClientes(request):
    ID_cliente=request.POST["numID_cliente"]
    Nombre=request.POST["txtNombre"]
    Correo=request.POST["txtCorreo"]
    Forma_de_pago=request.POST["txtForma_de_pago"]
    Productos=request.POST["txtProductos"]
    Saldo=request.POST["numSaldo"]
    Direccion=request.POST["txtDireccion"]
    clientes=Clientes.objects.get(ID_cliente=ID_cliente)
    clientes.Nombre=Nombre
    clientes.Correo=Correo
    clientes.Forma_de_pago=Forma_de_pago
    clientes.Productos=Productos
    clientes.Saldo=Saldo
    clientes.Direccion=Direccion
    clientes.save() #guarda registro actualizado
    return redirect("/")

def borrarClientes(request,ID_cliente):
    clientes=Clientes.objects.get(ID_cliente=ID_cliente)
    clientes.delete() # borra el registro
    return redirect("/")