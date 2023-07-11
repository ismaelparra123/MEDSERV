from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request,'core/home.html')

def convenios(request):

    return render(request,'core/convenios.html')

def productos(request):

    return render(request,'core/productos.html')

def login(request):

    return render(request,'core/login.html')

def registro(request):

    return render(request,'core/registro.html')

def carrito (request):
    return render(request, 'core/carrito.html')

def detalle_productores (request):
    return render(request,'core/detalle_productores.html')

def API (request):
    return render(request, 'core/API.html')