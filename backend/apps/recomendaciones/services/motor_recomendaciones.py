"""
motor_recomendaciones.py — Motor de recomendaciones personalizado.
Genera recomendaciones a partir del diagnóstico facial y el perfil del usuario.
Implementación completa en sprint de Motor de Recomendaciones.
"""

from apps.analisis.models import Diagnostico, NivelProblema


class MotorRecomendaciones:
    """
    Genera recomendaciones personalizadas a partir del diagnóstico
    facial y el perfil de piel del usuario.

    Estructura de retorno estándar (definida en contexto v1.0):
    {
        'tipo_piel': str,
        'problemas_detectados': [...],
        'rutina_manana': [...],
        'rutina_noche': [...],
        'productos_recomendados': [...],
        'tratamientos_esteticos': [...],
        'maquillaje_recomendado': [...],
        'alerta_dermatologo': bool,
    }
    """

    def __init__(self, diagnostico: Diagnostico, perfil_piel):
        self.diagnostico = diagnostico
        self.perfil = perfil_piel

    def generar(self) -> dict:
        """Punto de entrada principal — retorna el dict estándar."""
        resultado = {
            'tipo_piel':               self.diagnostico.tipo_piel_detectado,
            'problemas_detectados':    self._detectar_problemas(),
            'rutina_manana':           self._generar_rutina_manana(),
            'rutina_noche':            self._generar_rutina_noche(),
            'productos_recomendados':  self._recomendar_productos(),
            'tratamientos_esteticos':  self._recomendar_tratamientos(),
            'maquillaje_recomendado':  self._recomendar_maquillaje(),
            'alerta_dermatologo':      self._evaluar_alerta_dermatologo(),
        }
        return resultado

    # ── Métodos internos ──────────────────────────────────────────────────────

    def _detectar_problemas(self) -> list:
        """Lista los problemas detectados con nivel y zona."""
        d = self.diagnostico
        problemas = []
        campos = [
            ('acne',    d.nivel_acne,    'general'),
            ('manchas', d.nivel_manchas, 'general'),
            ('arrugas', d.nivel_arrugas, 'general'),
            ('poros',   d.nivel_poros,   'nariz'),
            ('brillo',  d.nivel_brillo,  'zona-T'),
            ('ojeras',  d.nivel_ojeras,  'ojos'),
        ]
        for tipo, nivel, zona in campos:
            if nivel and nivel != NivelProblema.NINGUNO:
                problemas.append({'tipo': tipo, 'nivel': nivel, 'zona': zona})
        return problemas

    def _generar_rutina_manana(self) -> list:
        """
        Genera rutina de mañana según tipo de piel y problemas.
        STUB: implementación completa en sprint de recomendaciones.
        """
        return [
            'Limpiador facial suave',
            'Tónico equilibrante',
            'Sérum vitamina C',
            'Hidratante ligero',
            'Protector solar SPF 50',
        ]

    def _generar_rutina_noche(self) -> list:
        """
        Genera rutina de noche según tipo de piel y problemas.
        STUB: implementación completa en sprint de recomendaciones.
        """
        return [
            'Limpieza doble (aceite + gel)',
            'Tónico hidratante',
            'Sérum retinol o niacinamida',
            'Crema hidratante nutritiva',
            'Contorno de ojos',
        ]

    def _recomendar_productos(self) -> list:
        """STUB: retorna lista vacía hasta integrar catálogo de productos."""
        return []

    def _recomendar_tratamientos(self) -> list:
        """
        Sugiere tratamientos estéticos según nivel de problemas.
        Regla: flacidez severa → HIFU, Morpheus8, Radiofrecuencia.
        """
        tratamientos = []
        if self.diagnostico.nivel_arrugas == NivelProblema.SEVERO:
            tratamientos.extend(['HIFU', 'Morpheus8', 'Radiofrecuencia'])
        return tratamientos

    def _recomendar_maquillaje(self) -> list:
        """STUB: retorna lista vacía hasta integrar catálogo de maquillaje."""
        return []

    def _evaluar_alerta_dermatologo(self) -> bool:
        """
        SEGURIDAD DERMATOLÓGICA:
        Siempre True si acné o manchas son severos.
        """
        return (
            self.diagnostico.nivel_acne    == NivelProblema.SEVERO or
            self.diagnostico.nivel_manchas == NivelProblema.SEVERO
        )
