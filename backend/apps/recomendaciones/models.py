"""
models.py — App recomendaciones
Modelos: Recomendacion, Rutina
"""

from django.db import models
from django.conf import settings


class Recomendacion(models.Model):
    """
    Recomendación generada por el motor para un diagnóstico.
    Puede referir a un producto, tratamiento, maquillaje o rutina.
    """

    class Tipo(models.TextChoices):
        PRODUCTO     = 'producto',     'Producto'
        TRATAMIENTO  = 'tratamiento',  'Tratamiento'
        MAQUILLAJE   = 'maquillaje',   'Maquillaje'
        RUTINA       = 'rutina',       'Rutina'

    diagnostico = models.ForeignKey(
        'analisis.Diagnostico',
        on_delete=models.CASCADE,
        related_name='recomendaciones',
        verbose_name='Diagnóstico',
    )
    tipo = models.CharField(
        max_length=15,
        choices=Tipo.choices,
        verbose_name='Tipo de recomendación',
    )
    referencia_id = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='ID del producto/tratamiento referenciado',
    )
    razon = models.TextField(verbose_name='Razón de la recomendación')
    prioridad = models.PositiveSmallIntegerField(
        default=1,
        verbose_name='Prioridad (1=alta)',
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Recomendación'
        verbose_name_plural = 'Recomendaciones'
        ordering = ['prioridad']

    def __str__(self):
        return f'Recomendación [{self.tipo}] para diagnóstico #{self.diagnostico_id}'


class Rutina(models.Model):
    """
    Rutina de cuidado personalizada para un usuario.
    Generada por el motor de recomendaciones.
    """

    class Frecuencia(models.TextChoices):
        DIARIA   = 'diaria',   'Diaria'
        SEMANAL  = 'semanal',  'Semanal'

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='rutinas',
        verbose_name='Usuario',
    )
    diagnostico = models.ForeignKey(
        'analisis.Diagnostico',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='rutinas',
        verbose_name='Diagnóstico de origen',
    )
    frecuencia = models.CharField(
        max_length=8,
        choices=Frecuencia.choices,
        default=Frecuencia.DIARIA,
        verbose_name='Frecuencia',
    )
    # JSONField: lista ordenada de pasos (strings)
    pasos_manana = models.JSONField(default=list, verbose_name='Pasos de mañana')
    pasos_noche  = models.JSONField(default=list, verbose_name='Pasos de noche')
    activa = models.BooleanField(default=True, verbose_name='Rutina activa')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Rutina'
        verbose_name_plural = 'Rutinas'
        ordering = ['-created_at']

    def __str__(self):
        return f'Rutina {self.frecuencia} de {self.usuario}'
