from django.contrib import admin
from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'categoria', 'precio', 'stock', 'estado', 'creado_en')
    list_filter = ('estado', 'categoria')
    search_fields = ('codigo', 'nombre')