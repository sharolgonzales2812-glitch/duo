"""admin.py — App progreso"""

from django.contrib import admin
from .models import RegistroProgreso


@admin.register(RegistroProgreso)
class RegistroProgresoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'fecha', 'diagnostico_asociado')
    search_fields = ('usuario__correo', 'usuario__nombre')
    list_filter = ('fecha',)
