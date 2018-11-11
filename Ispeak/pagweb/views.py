from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Diccionario
# Create your views here.


def index(request): #Cargar index
    usuario = request.session.get('usuario',None)
    return render(request,'index.html',{})

def login(request):
    return render(request, 'login.html',{}) #Mostrar login

def diccionario(request):
    return render(request, 'Diccionario.html',{}) #Mostrar diccionario

def contactos(request):
    return render(request, 'contactos.html',{}) #Redireccionar contactos

def noticia1(request):
    return render(request, 'noticia1.html', {}) #mostrar noticia 1

def noticia2(request):
    return render(request, 'noticia2.html', {}) #mostrar noticia 2

def noticia3(request):
    return render(request, 'noticia3.html', {}) #mostrar noticia 3

def modificar(request):
    español = request.POST.get('buscarEspañol', 'vacio')
    try:
        palabra = Diccionario.objects.get(español = español)
    except:
        palabra = Diccionario(español = "vacio", portuges = "vacio", ingles = "vacio", creolles = "vacio")

    return render(request, 'modificar.html',{'palabra':palabra})

def login_iniciar(request):
    correo = request.POST.get('nombre_usuario', '')
    contrasenia = request.POST.get('contrasenia', '')
    persona = Persona.objects.filter(correo=correo).filter(contrasenia=contrasenia)
    print(persona)
    if persona is not None:
        request.session['usuario'] = persona[0].nombre
        request.session['id'] = persona[0].id
        return redirect('index')
    else:
        return HttpResponse('No existe')

def traducido(request):
    español = request.POST.get('traducirEspañol','vacio')
    try:
        palabra = Diccionario.objects.get(español = español)
    except:
        palabra = Diccionario(español = "vacio", portuges = "vacio", ingles = "vacio", creolles = "vacio")

    return render(request, 'Diccionario.html', {'palabra':palabra})

def agregarPalabra(request):
    español = request.POST.get('agregarEspañol','vacio')
    portuges = request.POST.get('agregarPortuges','vacio')
    ingles = request.POST.get('agregarIngles', 'vacio')
    creolles = request.POST.get('agregarCreolles', 'vacio')

    try:
        buscar_palabra = Diccionario.objects.filter(español = español)
        palabra = Diccionario(español = español, portuges = portuges, ingles = ingles, creolles = creolles)
        palabra.save()
        return redirect('diccionario')
    except:
        return HttpResponse('Error! no se puede agregar la palabra deseada.')

def modificarPalabra(request):
    español = request.POST.get('modificarEspañol','vacio')
    portuges = request.POST.get('modificarPortuges','vacio')
    ingles = request.POST.get('modificarIngles', 'vacio')
    creolles = request.POST.get('modificarCreolles', 'vacio')
    
    try:
        palabra = Diccionario.objects.get(español = español)

        palabra.español = español
        palabra.portuges = portuges
        palabra.ingles = ingles
        palabra.creolles = creolles

        palabra.save()
        return redirect('diccionario')
    except:
        return HttpResponse('Error! no existe la palabra que desea modificar.')

def eliminarPalabra(request):
    español = request.POST.get('eliminarEspañol','vacio')
    try:
        palabra = Diccionario.objects.get(español = español)
        palabra.delete()
        return redirect('diccionario')
    except:
        return HttpResponse('Error! no se puedo eliminar la palabra')
