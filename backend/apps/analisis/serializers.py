"""
serializers.py — App analisis
"""

from rest_framework import serializers
from .models import Diagnostico, MetricaFacial


class MetricaFacialSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetricaFacial
        fields = ('id', 'nombre_metrica', 'valor', 'unidad')


class DiagnosticoSerializer(serializers.ModelSerializer):
    metricas = MetricaFacialSerializer(many=True, read_only=True)
    requiere_dermatologo = serializers.BooleanField(read_only=True)

    class Meta:
        model = Diagnostico
        fields = (
            'id', 'usuario', 'imagen_original', 'fecha',
            'tipo_piel_detectado',
            'nivel_acne', 'nivel_manchas', 'nivel_arrugas',
            'nivel_poros', 'nivel_brillo', 'nivel_ojeras',
            'observaciones', 'tiempo_procesamiento_ms',
            'requiere_dermatologo', 'metricas',
            'created_at',
        )
        read_only_fields = ('id', 'fecha', 'created_at', 'requiere_dermatologo')


class ImagenFacialSerializer(serializers.ModelSerializer):
    """Serializador de entrada: solo recibe la imagen para análisis."""

    class Meta:
        model = Diagnostico
        fields = ('imagen_original',)

    def save(self, **kwargs):
        return Diagnostico(**{**self.validated_data, **kwargs})
