from django.db import models

class Perfil_Profesional(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()
    carrera = models.CharField(max_length=100)
    celular = models.CharField(max_length=20)