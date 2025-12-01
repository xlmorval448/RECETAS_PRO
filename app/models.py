from django.db import models

# Create your models here.

class CategoriaIngrediente(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre}"


class Ingrediente(models.Model):
    class MercadoOpcion(models.TextChoices):
        MERCADONA = 'MER', 'Mercadona'
        CARREFOUR = 'CAR', 'Carrefour'
        LIDL = 'LID', 'Lidl'
        DIA = 'DIA', 'Dia'
        PLAZA = 'PLA', 'Mercado de Abastos'
        OTRO = 'OTR', 'Otro'

    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(CategoriaIngrediente, on_delete=models.CASCADE)
    mercado_habitual = models.CharField(choices=MercadoOpcion.choices, null=True,blank=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.categoria})"