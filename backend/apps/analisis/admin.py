"""admin.py — App analisis"""

from django.contrib import admin
from .models import Diagnostico, MetricaFacial


class MetricaFacialInline(admin.TabularInline):
    model = MetricaFacial
    extra = 0
    readonly_fields = ('nombre_metrica', 'valor', 'unidad')


@admin.register(Diagnostico)
class DiagnosticoAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'usuario', 'tipo_piel_detectado',
        'nivel_acne', 'nivel_manchas', 'requiere_dermatologo', 'fecha',
    )
    list_filter = ('tipo_piel_detectado', 'nivel_acne', 'nivel_manchas')
    search_fields = ('usuario__correo', 'usuario__nombre')
    readonly_fields = ('fecha', 'tiempo_procesamiento_ms', 'requiere_dermatologo')
    inlines = [MetricaFacialInline]
