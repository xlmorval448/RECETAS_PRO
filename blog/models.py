from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    #autor = models.CharField(max_length=60)
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
    cuerpo = models.TextField()

    def __str__(self):
        return f"({self.id}) {self.titulo}"

class Autor(models.Model):
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nombre