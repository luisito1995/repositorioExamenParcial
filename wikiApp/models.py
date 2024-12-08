from django.db import models

# Create your models here.

class tema(models.Model):
    nombreTema = models.CharField(max_length=128, null=True, blank=True)
    descripcionTema = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return self.nombreTema

class Articulo(models.Model):
    tituloArticulo = models.CharField(max_length=128)
    contenidoArticulo = models.TextField(max_length=1024)
    tema = models.ForeignKey(tema, on_delete=models.CASCADE)  # Relación con el modelo Tema

    def __str__(self):
        return self.tituloArticulo