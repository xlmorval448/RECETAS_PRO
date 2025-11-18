from django.db import models

# Create your models here.

# class CategoriaChoises(models.TextChoices):
#     LEGUMBRE = 'LE', "Legumbres"

class CategoriaIngredientes(models.Model):
    nombre = models.CharField(max_length=50)

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    # categoria = models.CharField(max_length=2, choices=CategoriaChoises, default=CategoriaChoises.LEGUMBRE)
    categoria = models.ForeignKey('CategoriaIngredientes', on_delete=models.CASCADE)
