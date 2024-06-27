from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Use(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Instrument(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    creation_date = models.DateField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    use = models.ForeignKey(Use, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    url_imagen = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
