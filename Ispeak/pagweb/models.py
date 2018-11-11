from django.db import models

# Create your models here.

class Diccionario(models.Model):
    español = models.CharField(max_length = 50)
    portuges = models.CharField(max_length = 50)
    creolles = models.CharField(max_length = 50)
    ingles = models.CharField(max_length = 50)
