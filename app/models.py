from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Evento (models.Model):

     nombre = models.CharField(max_length=50)
     lugar = models.CharField(max_length=50)
     requisitos = models.TextField()
     transporte = models.BooleanField()
     fecha = models.DateField()

     def __str__(self):
        return self.nombre 


class CrearEvento (models.Model):

     nombre = models.CharField(max_length=50)
     lugar = models.CharField(max_length=50)
     requisitos = models.TextField()
     transporte = models.BooleanField()
     fecha = models.DateField()

     def __str__(self):
        return self.nombre 



