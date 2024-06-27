from rest_framework import generics
from instruments.models import Instrument
from instruments.serializers.catalogs_serializer import InstrumentSerializer

class InstrumentList(generics.ListCreateAPIView):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name', None)
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)
        type = self.request.query_params.get('type', None)
        brand = self.request.query_params.get('brand', None)
        material = self.request.query_params.get('material', None)
        use = self.request.query_params.get('use', None)

        if name:
            queryset = queryset.filter(nombre__icontains=name)
        if min_price:
            queryset = queryset.filter(precio__gte=min_price)
        if max_price:
            queryset = queryset.filter(precio__lte=max_price)
        if type:
            queryset = queryset.filter(tipo_id=type)
        if brand:
            queryset = queryset.filter(marca_id=brand)
        if material:
            queryset = queryset.filter(material_id=material)
        if use:
            queryset = queryset.filter(uso_id=use)
        
        return queryset

class InstrumentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer
  