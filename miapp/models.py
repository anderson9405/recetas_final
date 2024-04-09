from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Receta(models.Model):
    nombre= models.CharField(max_length=200)
    ingredientes= models.TextField()
    descripcion= models.TextField()

    def __str__(self) -> str:
        return self.nombre + '-' + self.ingredientes+ '-' + self.descripcion