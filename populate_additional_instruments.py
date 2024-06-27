import os
import django
import random
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tienda_instrumentos.settings')
django.setup()

from instrumentos.models import Tipo, Marca, Material, Uso, Instrumento

# Datos adicionales para los instrumentos
nombres_instrumentos = [
    'Piano de Cola', 'Saxofón Alto', 'Trompeta', 'Trombón', 'Bajo Eléctrico', 
    'Clarinete', 'Flauta Traversa', 'Timbal', 'Violoncelo', 'Arpa', 
    'Teclado', 'Batería Electrónica', 'Viola', 'Guitarra Eléctrica', 'Mandolina'
]

# Obtener instancias de los tipos, marcas, materiales y usos existentes
tipos = list(Tipo.objects.all())
marcas = list(Marca.objects.all())
materiales = list(Material.objects.all())
usos = list(Uso.objects.all())

# Generar 15 instrumentos adicionales
for nombre in nombres_instrumentos:
    precio = round(random.uniform(100, 2000), 2)
    fecha_creacion = date.today()
    tipo = random.choice(tipos)
    marca = random.choice(marcas)
    material = random.choice(materiales)
    uso = random.choice(usos)
    descripcion = f'Un {nombre.lower()} de excelente calidad de la marca {marca.nombre}.'
    imagen_url = 'http://example.com/images/default.jpg'

    Instrumento.objects.create(
        nombre=nombre,
        precio=precio,
        fecha_creacion=fecha_creacion,
        tipo=tipo,
        marca=marca,
        material=material,
        uso=uso,
        descripcion=descripcion,
        imagen_url=imagen_url
    )

print('15 instrumentos adicionales generados exitosamente.')
