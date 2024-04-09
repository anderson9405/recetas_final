from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Receta
from .forms import crearNuevaReceta


# Create your views here.
def index(request):
    return render(request, 'index.html')

def recetas(request):
    lista_recetas = list(Receta.objects.all())
    return render(request, 'recetas.html',{
        'recetas': lista_recetas
    })
           
    
def crear_receta(request):
    if(request.method == 'GET'):
        return render(request, 'crear_receta.html', {
            'form': crearNuevaReceta
        })
    else:
        Receta.objects.create(nombre=request.POST['nombre'], ingredientes=request.POST['ingredientes'],
                              descripcion=request.POST['descripcion'])
        return redirect ('recetas')
    

def recetas_detalle(request, id):
    receta= Receta.objects.get(id=id)
    return render(request, 'detalle.html',{
        'receta': receta
    })
