from django.shortcuts import render
from rest_framework import viewsets
from .models import Material, Categoria, Marca, Proveedor
from .serializers import MaterialSerializar, CategoriaSerializar, MarcaSerializar, ProveedorSerializar
from drf_spectacular.utils import extend_schema

# Create your views here.
@extend_schema(tags=['Materiales'])
class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializar

@extend_schema(tags=['Categorias'])
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializar

@extend_schema(tags=['Marcas'])
class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializar

@extend_schema(tags=['Proveedores'])
class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializar