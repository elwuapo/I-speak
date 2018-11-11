from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name="index"),
    path('login',views.login, name="login"),
    path('diccionario/', views.diccionario, name= "diccionario"),
    path('diccionario/traducido/', views.traducido, name= "traducido"),
    path('diccionario/modificar/', views.modificar, name= "modificar"),
    path('diccionario/modificar/agregado/', views.agregarPalabra, name= "agregarPalabra"),
    path('diccionario/modificar/modificado/', views.modificarPalabra, name= "modificarPalabra"),
    path('diccionario/modificar/eliminado/', views.eliminarPalabra, name= "eliminarPalabra"),

]
