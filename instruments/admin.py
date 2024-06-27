from django.contrib import admin
from .models import Type, Brand, Material, Use, Instrument

admin.site.register(Type)
admin.site.register(Brand)
admin.site.register(Material)
admin.site.register(Use)
admin.site.register(Instrument)

# Register your models here.
