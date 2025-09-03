from rest_framework import serializers
from .models import Material, Categoria, Marca, Proveedor

class MaterialSerializar(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

class CategoriaSerializar(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class MarcaSerializar(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class ProveedorSerializar(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'