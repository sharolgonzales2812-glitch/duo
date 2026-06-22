"""serializers.py — App progreso"""

from rest_framework import serializers
from .models import RegistroProgreso


class RegistroProgresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroProgreso
        fields = (
            'id', 'usuario', 'fecha', 'imagen',
            'diagnostico_asociado', 'notas', 'created_at',
        )
        read_only_fields = ('id', 'usuario', 'fecha', 'created_at')
