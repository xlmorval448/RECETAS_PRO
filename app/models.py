from django.db import models

# Create your models here.

class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    ingredientes = models.ManyToManyField("Ingrediente", related_name='recetas', through="IngredienteReceta")

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
    mercado_habitual = models.CharField(max_length=3, choices=MercadoOpcion.choices, null=True,blank=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.categoria})"


class IngredienteReceta(models.Model):
    class UnidadesChoices(models.TextChoices):
        MILILITRO = 'ml', 'Mililitro'
        LITRO = 'l', 'Litro'
        MILIGRAMO = 'mg', 'miligramo'
        GRAMO = 'gr', 'Gramo'
        KILOGRAMO = 'kg', 'kilogramo'

    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    medida = models.CharField(max_length=2, choices=UnidadesChoices.choices)
    
    class Meta:
        unique_together = ('receta', 'ingrediente')
