from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import tema, Articulo


# Create your views here.
def temas(request):
    temasTotales = tema.objects.all()
    return render(request,'temas.html',{
        'temasTotales':temasTotales
    })

def vistaPrincipal(request):
    temasTotales = tema.objects.all()  # Obtener todos los temas
    return render(request, 'vistaPrincipal.html', {
        'temasTotales': temasTotales  # Pasar los temas al contexto
    })

def nuevoTema(request):
    if request.method == "POST":
        nombreTema = request.POST.get('nombreTema')
        descripcionTema = request.POST.get('descripcionTema')

        # Crear y guardar el nuevo tema
        nuevo_tema = tema(nombreTema=nombreTema, descripcionTema=descripcionTema)
        nuevo_tema.save()

        # Redirigir después de guardar el tema
        return redirect('wikiApp:nuevoTema')  # Puedes redirigir a donde quieras

    # Si el método no es POST, solo renderiza el formulario vacío
    temasTotales = tema.objects.all()
    return render(request, 'nuevoTema.html', {'temasTotales': temasTotales})


def nuevoArticulo(request):
    temasTotales = tema.objects.all()  # Obtener todos los temas registrados
    if request.method == 'POST':
        # Obtener los datos del formulario
        tituloArticulo = request.POST.get('tituloArticulo')
        contenidoArticulo = request.POST.get('contenidoArticulo')
        tema_seleccionado_id = request.POST.get('tema')  # El ID del tema seleccionado en el formulario
        tema_seleccionado = tema.objects.get(id=tema_seleccionado_id)  # Obtener el objeto tema correspondiente al ID

        # Crear el artículo y asociarlo al tema seleccionado
        articulo = Articulo(tituloArticulo=tituloArticulo, contenidoArticulo=contenidoArticulo, tema=tema_seleccionado)
        articulo.save()  # Guardar el artículo en la base de datos

        # Redirigir después de guardar el artículo
        return redirect('wikiApp:nuevoArticulo')  # Puedes redirigir a donde quieras

    return render(request, 'nuevoArticulo.html', {'temasTotales': temasTotales})


def articuloxTema(request, tema_id=None):
    temas = tema.objects.all()
    articulos = Articulo.objects.filter(tema_id=tema_id) if tema_id else Articulo.objects.none()
    return render(request, 'articuloxTema.html', {
        'temasTotales': temas,
        'articulosFiltrados': articulos,
    })


def vistaArticulos(request):
    articulosTotales = Articulo.objects.select_related('tema').all()
    temasTotales = tema.objects.all()
    return render(request, 'vistaArticulos.html', {
        'articulosTotales': articulosTotales,
        'temasTotales': temasTotales
    })


def vistaBusqueda(request):
    # Obtenemos todos los temas para mostrar en la barra lateral
    temasTotales = tema.objects.all()
    
    # Si hay una búsqueda, filtramos los artículos por el título
    query = request.GET.get('query', '')
    if query:
        articulosCoincidencia = Articulo.objects.filter(tituloArticulo__icontains=query)
    else:
        articulosCoincidencia = Articulo.objects.none()  # Si no hay búsqueda, no mostramos artículos
    
    # Renderizamos la vista pasando los temas y los artículos encontrados
    return render(request, 'vistaBusqueda.html', {
        'temasTotales': temasTotales,
        'articulosCoincidencia': articulosCoincidencia,
    })