from django.db import models

class Tipo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Material(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Uso(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Instrumento(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateField()
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    uso = models.ForeignKey(Uso, on_delete=models.CASCADE)
    descripcion = models.TextField(null=True, blank=True)
    imagen_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nombre
# Create your models here.
