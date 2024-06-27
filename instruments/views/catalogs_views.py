from rest_framework import generics
from instruments.models import Type, Brand, Material, Use
from instruments.serializers.catalogs_serializer import TypeSerializer, BrandSerializer, MaterialSerializer, UseSerializer

class TypeList(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class TypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class BrandList(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class BrandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class MaterialList(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class MaterialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class UseList(generics.ListCreateAPIView):
    queryset = Use.objects.all()
    serializer_class = UseSerializer

class UseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Use.objects.all()
    serializer_class = UseSerializer
