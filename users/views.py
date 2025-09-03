from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RolSerializar, UsuarioSerializar
from .models import Rol, Usuario
from drf_spectacular.utils import extend_schema

# Create your views here.
@extend_schema(tags=['Roles'])
class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializar

@extend_schema(tags=['Users'])
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializar