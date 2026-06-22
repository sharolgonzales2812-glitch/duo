"""serializers.py — App recomendaciones"""

from rest_framework import serializers
from .models import Recomendacion, Rutina


class RecomendacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recomendacion
        fields = ('id', 'tipo', 'referencia_id', 'razon', 'prioridad', 'created_at')
        read_only_fields = ('id', 'created_at')


class RutinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rutina
        fields = (
            'id', 'usuario', 'diagnostico', 'frecuencia',
            'pasos_manana', 'pasos_noche', 'activa',
            'created_at', 'updated_at',
        )
        read_only_fields = ('id', 'usuario', 'created_at', 'updated_at')
