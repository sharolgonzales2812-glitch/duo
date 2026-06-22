"""
models.py — App productos
Modelos: Ingrediente, Producto, Tratamiento
"""

from django.db import models


class Ingrediente(models.Model):
    """Ingrediente activo de un producto cosmético."""
    nombre = models.CharField(max_length=100, unique=True, verbose_name='Nombre')
    funcion = models.CharField(max_length=200, verbose_name='Función principal')
    descripcion = models.TextField(blank=True, verbose_name='Descripción')
    contraindicaciones = models.TextField(blank=True, verbose_name='Contraindicaciones')

    class Meta:
        verbose_name = 'Ingrediente'
        verbose_name_plural = 'Ingredientes'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    """Producto de skincare del catálogo."""

    class Categoria(models.TextChoices):
        LIMPIADOR   = 'limpiador',   'Limpiador'
        TONICO      = 'tonico',      'Tónico'
        SERUM       = 'serum',       'Sérum'
        HIDRATANTE  = 'hidratante',  'Hidratante'
        PROTECTOR   = 'protector',   'Protector solar'
        TRATAMIENTO = 'tratamiento', 'Tratamiento'
        CONTORNO    = 'contorno',    'Contorno de ojos'
        MASCARILLA  = 'mascarilla',  'Mascarilla'

    class TipoPielObjetivo(models.TextChoices):
        TODOS    = 'todos',    'Todos'
        NORMAL   = 'normal',   'Normal'
        SECA     = 'seca',     'Seca'
        GRASA    = 'grasa',    'Grasa'
        MIXTA    = 'mixta',    'Mixta'
        SENSIBLE = 'sensible', 'Sensible'

    nombre = models.CharField(max_length=200, verbose_name='Nombre')
    marca = models.CharField(max_length=100, verbose_name='Marca')
    categoria = models.CharField(
        max_length=15,
        choices=Categoria.choices,
        verbose_name='Categoría',
    )
    ingredientes = models.ManyToManyField(
        Ingrediente,
        related_name='productos',
        blank=True,
        verbose_name='Ingredientes',
    )
    tipo_piel_objetivo = models.CharField(
        max_length=10,
        choices=TipoPielObjetivo.choices,
        default=TipoPielObjetivo.TODOS,
        verbose_name='Tipo de piel objetivo',
    )
    precio = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Precio',
    )
    descripcion = models.TextField(blank=True, verbose_name='Descripción')
    imagen = models.ImageField(
        upload_to='productos/',
        null=True,
        blank=True,
        verbose_name='Imagen',
    )
    activo = models.BooleanField(default=True, verbose_name='Activo')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['categoria', 'nombre']

    def __str__(self):
        return f'{self.marca} — {self.nombre} ({self.categoria})'


class Tratamiento(models.Model):
    """Tratamiento estético avanzado del catálogo."""

    class TipoTratamiento(models.TextChoices):
        HIFU            = 'HIFU',           'HIFU'
        MORPHEUS8       = 'Morpheus8',      'Morpheus8'
        RADIOFRECUENCIA = 'Radiofrecuencia','Radiofrecuencia'
        LASER           = 'Laser',          'Láser'
        OTRO            = 'Otro',           'Otro'

    nombre = models.CharField(max_length=200, verbose_name='Nombre')
    tipo = models.CharField(
        max_length=20,
        choices=TipoTratamiento.choices,
        verbose_name='Tipo',
    )
    descripcion = models.TextField(blank=True, verbose_name='Descripción')
    nivel_flacidez_recomendado = models.CharField(
        max_length=10,
        choices=[('leve', 'Leve'), ('moderado', 'Moderado'), ('severo', 'Severo')],
        default='moderado',
        verbose_name='Nivel de flacidez recomendado',
    )
    precio_estimado = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Precio estimado',
    )
    activo = models.BooleanField(default=True, verbose_name='Activo')

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Tratamiento'
        verbose_name_plural = 'Tratamientos'

    def __str__(self):
        return f'{self.nombre} ({self.tipo})'
