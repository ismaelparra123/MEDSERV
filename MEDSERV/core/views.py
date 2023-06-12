from django.shortcuts import render
from .models import Producto

# Create your views here.

def home(request):

    return render(request,'core/home.html')

def productos(request):
    
    return render(request,'core/productos.html')