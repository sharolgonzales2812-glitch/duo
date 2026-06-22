"""
admin.py — App accounts
Registra Usuario y PerfilPiel en el panel de administración.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, PerfilPiel


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'correo', 'nombre', 'apellido', 'edad', 'genero', 'is_staff')
    search_fields = ('username', 'correo', 'nombre', 'apellido')
    ordering = ('-created_at',)
    fieldsets = UserAdmin.fieldsets + (
        ('Datos skincaremaysha', {
            'fields': ('correo', 'nombre', 'apellido', 'edad', 'genero'),
        }),
    )


@admin.register(PerfilPiel)
class PerfilPielAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo_piel_declarado', 'presupuesto', 'cuestionario_completado')
    search_fields = ('usuario__correo', 'usuario__nombre')
    list_filter = ('tipo_piel_declarado', 'presupuesto', 'cuestionario_completado')
