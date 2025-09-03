from .models import Rol, Usuario
from rest_framework import serializers

class RolSerializar(serializers.ModelSerializer):
    class Meta:
        model =  Rol
        fields = '__all__'

class UsuarioSerializar(serializers.ModelSerializer):
    class Meta:
        model =  Usuario
        fields = '__all__'

        
