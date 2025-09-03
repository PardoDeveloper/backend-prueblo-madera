from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MaterialViewSet, CategoriaViewSet, MarcaViewSet, ProveedorViewSet

router = DefaultRouter()
router.register(r'materiales', MaterialViewSet, basename='materiales')
router.register(r'categorias', CategoriaViewSet, basename='categorias')
router.register(r'marcas', MarcaViewSet, basename='marcas')
router.register(r'proveedores', ProveedorViewSet, basename='proveedores')

urlpatterns = [
	path('api/', include(router.urls)),
]