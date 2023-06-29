from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request,'core/home.html')

def convenios(request):

    return render(request,'core/convenios.html')

def nosotros(request):

    return render(request,'core/nosotros.html')

def productos(request):

    return render(request,'core/productos.html')

def login(request):

    return render(request,'core/login.html')