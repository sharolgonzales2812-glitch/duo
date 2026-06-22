"""serializers.py — App productos"""

from rest_framework import serializers
from .models import Ingrediente, Producto, Tratamiento


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ('id', 'nombre', 'funcion', 'descripcion', 'contraindicaciones')


class ProductoSerializer(serializers.ModelSerializer):
    ingredientes = IngredienteSerializer(many=True, read_only=True)

    class Meta:
        model = Producto
        fields = (
            'id', 'nombre', 'marca', 'categoria', 'ingredientes',
            'tipo_piel_objetivo', 'precio', 'descripcion', 'imagen', 'activo',
        )


class TratamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamiento
        fields = (
            'id', 'nombre', 'tipo', 'descripcion',
            'nivel_flacidez_recomendado', 'precio_estimado', 'activo',
        )
