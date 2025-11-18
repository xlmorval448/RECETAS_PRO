from django.db import models

# Create your models here.

# class CategoriaChoises(models.TextChoices):
#     LEGUMBRE = 'LE', "Legumbres"

class CategoriaIngrediente(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id} {self.nombre}"

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    # categoria = models.CharField(max_length=2, choices=CategoriaChoises, default=CategoriaChoises.LEGUMBRE)
    categoria = models.ForeignKey('CategoriaIngrediente', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} {self.nombre} {self.categoria}"