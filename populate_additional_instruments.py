import os
import django
import random
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'instruments_store.settings')
django.setup()

from instruments.models import Type, Brand, Material, Use, Instrument

# Datos adicionales para los instrumentos
nombres_instrumentos = [
    'Piano de Cola', 'Saxofón Alto', 'Trompeta', 'Trombón', 'Bajo Eléctrico', 
    'Clarinete', 'Flauta Traversa', 'Timbal', 'Violoncelo', 'Arpa', 
    'Teclado', 'Batería Electrónica', 'Viola', 'Guitarra Eléctrica', 'Mandolina'
]

# Datos para crear tipos, marcas, materiales y usos
tipos_data = ['Cuerda', 'Viento', 'Percusión', 'Tecla']
marcas_data = ['Yamaha', 'Gibson', 'Fender', 'Roland', 'Casio']
materiales_data = ['Madera', 'Metal', 'Plástico', 'Compuesto']
usos_data = ['Principiante', 'Profesional', 'Estudio', 'Concierto']

# Crear y obtener instancias de los tipos, marcas, materiales y usos
for tipo in tipos_data:
    Type.objects.get_or_create(name=tipo)

for marca in marcas_data:
    Brand.objects.get_or_create(name=marca)

for material in materiales_data:
    Material.objects.get_or_create(name=material)

for uso in usos_data:
    Use.objects.get_or_create(name=uso)

# Obtener instancias de los tipos, marcas, materiales y usos existentes
tipos = list(Type.objects.all())
marcas = list(Brand.objects.all())
materiales = list(Material.objects.all())
usos = list(Use.objects.all())

# Generar 15 instrumentos adicionales
for nombre in nombres_instrumentos:
    precio = round(random.uniform(100, 2000), 2)
    fecha_creacion = date.today()
    tipo = random.choice(tipos)
    marca = random.choice(marcas)
    material = random.choice(materiales)
    uso = random.choice(usos)
    descripcion = f'Un {nombre.lower()} de excelente calidad de la marca {marca.name}.'
    url_imagen = 'http://example.com/images/default.jpg'

    Instrument.objects.create(
        name=nombre,
        price=precio,
        creation_date=fecha_creacion,
        type=tipo,
        brand=marca,
        material=material,
        use=uso,
        description=descripcion,
        url_imagen=url_imagen
    )

print('15 instrumentos adicionales generados exitosamente.')
