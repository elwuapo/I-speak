from django.shortcuts import render, redirect

# Create your views here.


def index(request): #Cargar index
    usuario = request.session.get('usuario',None) 
    return render(request,'index.html',{})

def login(request):
    return render(request, 'login.html',{}) #Mostrar login

def diccionario(request):  
    return redirect(request, 'diccionario.html',{}) #Mostrar diccionario

def contactos(request):
    return redirect(request, 'contactos.html',{}) #Redireccionar contactos

def noticia1(request):
    return redirect(request, 'noticia1.html', {}) #mostrar noticia 1


def noticia2(request):
    return redirect(request, 'noticia2.html', {}) #mostrar noticia 2

def noticia3(request):
    return redirect(request, 'noticia3.html', {}) #mostrar noticia 3

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
    
def agregarPalabra(request):
    español = request.POST.get('agregarEspañol','Vacio')
    portuges = request.POST.get('agregarPortuges','Vacio')
    ingles = request.POST.get('agregarIngles', 'Vacio')
    creolles = request.POST.get('agregarCreolles', 'Vacio')

    palabra = Diccionario(español = español, portuges = portuges, ingles = ingles, creolles = creolles)

    palabra.save()

    return redirect('')

def modificarPalabra(request):
    español = request.POST.get('modificarEspañol','Vacio')
    portuges = request.POST.get('modificarPortuges','Vacio')
    ingles = request.POST.get('modificarIngles', 'Vacio')
    creolles = request.POST.get('modificarCreolles', 'Vacio')

    palabra = Diccionario.objects.get(español = español)

    palabra[0].español = español
    palabra[0].portugues = portugues
    palabra[0].ingles = ingles
    palabra[0].creolles = creolles

    palabra.save()

    return redirect('')

def eliminarPalabra(request):
    español = request.POST.get('eliminarEspañol','Vacio')
    palabra = Diccionario.objects.get(español = español)
    palabra[0].save()

    return redirect('')


