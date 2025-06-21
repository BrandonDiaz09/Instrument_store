from rest_framework import serializers
from instruments.models import Type, Brand, Material, Use, Instrument

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

class UseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Use
        fields = '__all__'

class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = '__all__'

class InstrumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name']

class InstrumentBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']

class InstrumentMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'name']

class InstrumentUseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Use
        fields = ['id', 'name']

class InstrumentSerializer(serializers.ModelSerializer):
    type = InstrumentTypeSerializer()
    brand = InstrumentBrandSerializer()
    material = InstrumentMaterialSerializer()
    use = InstrumentUseSerializer()

    class Meta:
        model = Instrument
        fields = ['id', 'name', 'price', 'creation_date', 'type', 'brand', 'material', 'use', 'description', 'url_imagen']

