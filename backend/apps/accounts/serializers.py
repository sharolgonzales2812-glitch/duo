"""
serializers.py — App accounts
Serializadores: RegistroSerializer, PerfilPielSerializer, UsuarioSerializer
"""

from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import Usuario, PerfilPiel


class RegistroSerializer(serializers.ModelSerializer):
    """Registro de un nuevo usuario con contraseña confirmada."""

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Usuario
        fields = ('username', 'correo', 'nombre', 'apellido', 'edad', 'genero',
                  'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'Las contraseñas no coinciden.'})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        usuario = Usuario.objects.create_user(**validated_data)
        # Crear perfil de piel vacío automáticamente
        PerfilPiel.objects.create(usuario=usuario)
        return usuario


class PerfilPielSerializer(serializers.ModelSerializer):
    """Lectura y actualización del perfil de piel del usuario."""

    class Meta:
        model = PerfilPiel
        fields = (
            'id', 'tipo_piel_declarado', 'presupuesto', 'clima_region',
            'sensibilidades_conocidas', 'alergias', 'cuestionario_completado',
            'created_at', 'updated_at',
        )
        read_only_fields = ('id', 'created_at', 'updated_at')


class UsuarioSerializer(serializers.ModelSerializer):
    """Datos públicos del usuario autenticado + perfil de piel embebido."""

    perfil_piel = PerfilPielSerializer(read_only=True)

    class Meta:
        model = Usuario
        fields = (
            'id', 'username', 'correo', 'nombre', 'apellido',
            'edad', 'genero', 'perfil_piel', 'created_at',
        )
        read_only_fields = ('id', 'created_at')
