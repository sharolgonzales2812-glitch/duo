"""
models.py — App progreso
Modelos: RegistroProgreso
"""

from django.db import models
from django.conf import settings


class RegistroProgreso(models.Model):
    """
    Entrada del historial de evolución de la piel del usuario.
    Permite comparativa fotográfica y seguimiento de métricas en el tiempo.
    """
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='registros_progreso',
        verbose_name='Usuario',
    )
    fecha = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    imagen = models.ImageField(
        upload_to='progreso/%Y/%m/',
        verbose_name='Fotografía de progreso',
    )
    diagnostico_asociado = models.ForeignKey(
        'analisis.Diagnostico',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='registros_progreso',
        verbose_name='Diagnóstico asociado',
    )
    notas = models.TextField(blank=True, verbose_name='Notas del usuario')

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Registro de Progreso'
        verbose_name_plural = 'Registros de Progreso'
        ordering = ['-fecha']

    def __str__(self):
        return f'Progreso de {self.usuario} — {self.fecha:%Y-%m-%d}'
