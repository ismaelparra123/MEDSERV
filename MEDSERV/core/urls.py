from django.urls import path
from .views import home,productos,convenios,login,registro,carrito,detalle_productores, API

urlpatterns = [
    path('',home,name="home"),
    path('productos',productos,name="productos"),
    path('convenios',convenios,name="convenios"),
    path('login',login,name="login"),
    path('registro',registro,name="registro"),
    path('detalle_productores',detalle_productores,name="detalle_productores"),
    path('carrito',carrito,name="carrito"),
    path('API',API,name="API"),
]