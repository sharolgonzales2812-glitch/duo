"""
models.py — App accounts
Modelos: Usuario (extiende AbstractUser), PerfilPiel
"""

from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    """
    Usuario personalizado del sistema skincaremaysha.
    Extiende AbstractUser agregando campos específicos del negocio.
    """
    correo = models.EmailField(unique=True, verbose_name='Correo electrónico')
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=100, verbose_name='Apellido')
    edad = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Edad')

    class Genero(models.TextChoices):
        FEMENINO = 'F', 'Femenino'
        MASCULINO = 'M', 'Masculino'
        OTRO = 'O', 'Otro'
        PREFIERO_NO_DECIR = 'N', 'Prefiero no decir'

    genero = models.CharField(
        max_length=1,
        choices=Genero.choices,
        null=True,
        blank=True,
        verbose_name='Género',
    )

    # Usamos correo como campo de login
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['correo', 'nombre', 'apellido']

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.nombre} {self.apellido} ({self.correo})'


class PerfilPiel(models.Model):
    """
    Perfil de piel del usuario. Relación 1:1 con Usuario.
    Se crea al completar el cuestionario inicial.
    """

    class TipoPiel(models.TextChoices):
        NORMAL   = 'normal',   'Normal'
        SECA     = 'seca',     'Seca'
        GRASA    = 'grasa',    'Grasa'
        MIXTA    = 'mixta',    'Mixta'
        SENSIBLE = 'sensible', 'Sensible'

    class Presupuesto(models.TextChoices):
        BAJO  = 'bajo',  'Bajo'
        MEDIO = 'medio', 'Medio'
        ALTO  = 'alto',  'Alto'

    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        related_name='perfil_piel',
        verbose_name='Usuario',
    )
    tipo_piel_declarado = models.CharField(
        max_length=10,
        choices=TipoPiel.choices,
        null=True,
        blank=True,
        verbose_name='Tipo de piel declarado',
    )
    presupuesto = models.CharField(
        max_length=5,
        choices=Presupuesto.choices,
        default=Presupuesto.MEDIO,
        verbose_name='Presupuesto',
    )
    clima_region = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Clima / Región',
    )
    sensibilidades_conocidas = models.TextField(
        blank=True,
        verbose_name='Sensibilidades conocidas',
    )
    alergias = models.TextField(
        blank=True,
        verbose_name='Alergias',
    )
    cuestionario_completado = models.BooleanField(
        default=False,
        verbose_name='Cuestionario completado',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Perfil de Piel'
        verbose_name_plural = 'Perfiles de Piel'

    def __str__(self):
        return f'Perfil de {self.usuario} — {self.tipo_piel_declarado}'
