from django.urls import path
from . import views

app_name='wikiApp'

urlpatterns = [
    path('',views.vistaPrincipal,name='vistaPrincipal'),
    path('nuevoTema',views.nuevoTema,name='nuevoTema'),
    path('nuevoArticulo',views.nuevoArticulo,name='nuevoArticulo'),
    path('articuloxTema/<int:tema_id>/', views.articuloxTema, name='articuloxTema'),
    path('vistaArticulos',views.vistaArticulos,name='vistaArticulos'),
    path('vistaBusqueda',views.vistaBusqueda,name='vistaBusqueda')
]
