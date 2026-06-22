"""admin.py — App productos"""

from django.contrib import admin
from .models import Ingrediente, Producto, Tratamiento


@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'funcion')
    search_fields = ('nombre', 'funcion')


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'categoria', 'tipo_piel_objetivo', 'precio', 'activo')
    list_filter = ('categoria', 'tipo_piel_objetivo', 'activo')
    search_fields = ('nombre', 'marca')
    filter_horizontal = ('ingredientes',)


@admin.register(Tratamiento)
class TratamientoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'nivel_flacidez_recomendado', 'precio_estimado', 'activo')
    list_filter = ('tipo', 'activo')
