"""
metricas_service.py — Extracción de métricas faciales.
Extrae 200+ métricas a partir de los resultados del VisionService.
STUB funcional — implementación completa en sprint de IA.
"""

from ..models import Diagnostico, MetricaFacial


class MetricasService:
    """
    Extrae y persiste métricas faciales individuales
    a partir de un diagnóstico ya guardado.

    Uso:
        servicio = MetricasService(diagnostico)
        servicio.extraer_y_guardar(resultados_vision)
    """

    def __init__(self, diagnostico: Diagnostico):
        self.diagnostico = diagnostico

    def extraer_y_guardar(self, resultados: dict) -> list:
        """
        Recibe el dict de resultados del VisionService,
        extrae métricas individuales y las guarda en BD.
        Retorna la lista de MetricaFacial creadas.
        """
        metricas_data = self._extraer_metricas(resultados)
        metricas_creadas = []
        for metrica in metricas_data:
            obj = MetricaFacial.objects.create(
                diagnostico=self.diagnostico,
                nombre_metrica=metrica['nombre'],
                valor=metrica['valor'],
                unidad=metrica.get('unidad', ''),
            )
            metricas_creadas.append(obj)
        return metricas_creadas

    def _extraer_metricas(self, resultados: dict) -> list:
        """
        STUB: retorna lista vacía.
        Implementación completa en sprint de IA.
        """
        return []
