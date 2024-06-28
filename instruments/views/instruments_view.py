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
            queryset = queryset.filter(name__icontains=name)
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        if type:
            type_ids = [int(t) for t in type.split(",")]
            queryset = queryset.filter(type_id__in=type_ids)
        if brand:
            brand_ids = [int(b) for b in brand.split(",")]
            queryset = queryset.filter(brand_id__in=brand_ids)
        if material:
            material_ids = [int(m) for m in material.split(",")]
            queryset = queryset.filter(material_id__in=material_ids)
        if use:
            use_ids = [int(u) for u in use.split(",")]
            queryset = queryset.filter(use_id__in=use_ids)

        queryset = queryset.order_by('price', 'creation_date')
        return queryset


class InstrumentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer
  