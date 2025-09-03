from rest_framework import serializers
from .models import Material, Categoria, Marca, Proveedor


class CategoriaSerializar(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nombre']

class MarcaSerializar(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['nombre']

class ProveedorSerializar(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ['nombre']

class MaterialSerializar(serializers.ModelSerializer):
    categoria = CategoriaSerializar()   # 👈 Se anida el serializador de Categoria
    marca = MarcaSerializar()           # 👈 Se anida el serializador de Marca
    proveedor = ProveedorSerializar() 
    class Meta:
        model = Material
        fields = '__all__'