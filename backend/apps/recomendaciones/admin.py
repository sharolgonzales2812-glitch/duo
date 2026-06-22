"""admin.py — App recomendaciones"""

from django.contrib import admin
from .models import Recomendacion, Rutina


@admin.register(Recomendacion)
class RecomendacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'diagnostico', 'prioridad', 'created_at')
    list_filter = ('tipo',)


@admin.register(Rutina)
class RutinaAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'frecuencia', 'activa', 'created_at')
    list_filter = ('frecuencia', 'activa')
