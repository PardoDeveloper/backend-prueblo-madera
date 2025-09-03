from django.contrib import admin
from .models import Categoria, Marca, Material, Proveedor

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Material)
admin.site.register(Proveedor)