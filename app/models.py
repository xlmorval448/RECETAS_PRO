from django.db import models

# Create your models here.

class Mercado(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    envio_a_domicilio = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre}"


class CategoriaIngrediente(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre}"


class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey('CategoriaIngrediente', on_delete=models.CASCADE)
    mercado_habitual = models.ForeignKey(Mercado, on_delete=models.CASCADE, null=True, blank=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.categoria})"