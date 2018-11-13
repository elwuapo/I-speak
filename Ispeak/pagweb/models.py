from django.db import models

# Create your models here.

class Diccionario(models.Model):
    español = models.CharField(max_length = 50)
    portuges = models.CharField(max_length = 50)
    creolles = models.CharField(max_length = 50)
    ingles = models.CharField(max_length = 50)

class Publicacion(models.Model):
    encabezado = models.CharField(max_length = 60)
    foto = models.ImageField(upload_to = 'foto/')
    cuerpo = models.TextField()
