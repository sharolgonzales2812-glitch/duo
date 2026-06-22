"""
models.py — App analisis
Modelos: Diagnostico, MetricaFacial
"""

from django.db import models
from django.conf import settings


class NivelProblema(models.TextChoices):
    """Choices reutilizables para nivel de cada problema detectado."""
    NINGUNO  = 'ninguno',   'Ninguno'
    LEVE     = 'leve',      'Leve'
    MODERADO = 'moderado',  'Moderado'
    SEVERO   = 'severo',    'Severo'


class Diagnostico(models.Model):
    """
    Resultado del análisis facial de un usuario.
    Generado por el VisionService tras procesar la imagen con YOLOv11 + OpenCV.
    """

    class TipoPiel(models.TextChoices):
        NORMAL   = 'normal',   'Normal'
        SECA     = 'seca',     'Seca'
        GRASA    = 'grasa',    'Grasa'
        MIXTA    = 'mixta',    'Mixta'
        SENSIBLE = 'sensible', 'Sensible'

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='diagnosticos',
        verbose_name='Usuario',
    )
    imagen_original = models.ImageField(
        upload_to='diagnosticos/%Y/%m/',
        verbose_name='Imagen original',
    )
    fecha = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')

    # Resultados del análisis de IA
    tipo_piel_detectado = models.CharField(
        max_length=10,
        choices=TipoPiel.choices,
        null=True,
        blank=True,
        verbose_name='Tipo de piel detectado',
    )
    nivel_acne = models.CharField(
        max_length=10, choices=NivelProblema.choices,
        default=NivelProblema.NINGUNO, verbose_name='Nivel de acné',
    )
    nivel_manchas = models.CharField(
        max_length=10, choices=NivelProblema.choices,
        default=NivelProblema.NINGUNO, verbose_name='Nivel de manchas',
    )
    nivel_arrugas = models.CharField(
        max_length=10, choices=NivelProblema.choices,
        default=NivelProblema.NINGUNO, verbose_name='Nivel de arrugas',
    )
    nivel_poros = models.CharField(
        max_length=10, choices=NivelProblema.choices,
        default=NivelProblema.NINGUNO, verbose_name='Nivel de poros',
    )
    nivel_brillo = models.CharField(
        max_length=10, choices=NivelProblema.choices,
        default=NivelProblema.NINGUNO, verbose_name='Nivel de brillo/oleosidad',
    )
    nivel_ojeras = models.CharField(
        max_length=10, choices=NivelProblema.choices,
        default=NivelProblema.NINGUNO, verbose_name='Nivel de ojeras',
    )
    observaciones = models.TextField(blank=True, verbose_name='Observaciones adicionales')
    tiempo_procesamiento_ms = models.IntegerField(
        default=0,
        verbose_name='Tiempo de procesamiento (ms)',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Diagnóstico'
        verbose_name_plural = 'Diagnósticos'
        ordering = ['-fecha']

    def __str__(self):
        return f'Diagnóstico #{self.pk} — {self.usuario} ({self.fecha:%Y-%m-%d})'

    @property
    def requiere_dermatologo(self):
        """True si algún problema es severo — alerta de seguridad dermatológica."""
        return self.nivel_acne == NivelProblema.SEVERO or \
               self.nivel_manchas == NivelProblema.SEVERO


class MetricaFacial(models.Model):
    """
    Métricas individuales extraídas del análisis facial (200+ métricas).
    Relación N:1 con Diagnostico.
    """
    diagnostico = models.ForeignKey(
        Diagnostico,
        on_delete=models.CASCADE,
        related_name='metricas',
        verbose_name='Diagnóstico',
    )
    nombre_metrica = models.CharField(max_length=100, verbose_name='Nombre de la métrica')
    valor = models.FloatField(verbose_name='Valor')
    unidad = models.CharField(max_length=30, blank=True, verbose_name='Unidad')

    class Meta:
        verbose_name = 'Métrica Facial'
        verbose_name_plural = 'Métricas Faciales'

    def __str__(self):
        return f'{self.nombre_metrica}: {self.valor} {self.unidad}'
