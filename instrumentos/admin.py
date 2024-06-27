from django.contrib import admin
from .models import Tipo, Marca, Material, Uso, Instrumento

admin.site.register(Tipo)
admin.site.register(Marca)
admin.site.register(Material)
admin.site.register(Uso)
admin.site.register(Instrumento)

# Register your models here.
