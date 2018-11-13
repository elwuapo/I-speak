from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name="index"),
    path('login',views.login, name="login"),
    path('login/iniciar',views.login_iniciar, name="iniciar"),
    path('cerrarsession',views.cerrar_session, name="cerrar_session"),
    path('diccionario/', views.diccionario, name= "diccionario"),
    path('diccionario/traducido/', views.traducido, name= "traducido"),
    path('diccionario/modificar/', views.modificar, name= "modificar"),
    path('diccionario/modificar/agregado/', views.agregarPalabra, name= "agregarPalabra"),
    path('diccionario/modificar/modificado/', views.modificarPalabra, name= "modificarPalabra"),
    path('diccionario/modificar/eliminado/', views.eliminarPalabra, name= "eliminarPalabra"),
    path('crearPost', views.crearPublicacion, name="crearPost")

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
