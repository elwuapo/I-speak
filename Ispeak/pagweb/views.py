from django.shortcuts import render, redirect

# Create your views here.
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
