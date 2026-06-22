"""
vision_service.py — Servicio de visión artificial.
Integra YOLOv11 + OpenCV para análisis facial.
Este archivo es un STUB funcional — la implementación completa del modelo
de IA se realiza en el sprint de Inteligencia Artificial.
"""

import time


class VisionService:
    """
    Procesa una imagen facial con YOLOv11 + OpenCV
    y retorna las métricas detectadas.

    Uso:
        servicio = VisionService()
        resultado = servicio.analizar('/ruta/a/imagen.jpg')
    """

    def __init__(self):
        self.model = self._cargar_modelo()

    def analizar(self, imagen_path: str) -> dict:
        """
        Recibe la ruta de la imagen guardada.
        Retorna dict con tipo_piel y niveles de cada problema detectado.
        """
        inicio = time.time()
        imagen = self._preprocesar_imagen(imagen_path)
        resultados_raw = self._inferir(imagen)
        resultado = self._postprocesar(resultados_raw)
        resultado['tiempo_procesamiento_ms'] = int((time.time() - inicio) * 1000)
        return resultado

    def _cargar_modelo(self):
        """
        Carga el modelo YOLOv11n desde disco.
        STUB: retorna None hasta que el modelo esté disponible.
        Implementación completa en sprint de IA:
            from ultralytics import YOLO
            return YOLO('models/yolov11n_skincare.pt')
        """
        return None

    def _preprocesar_imagen(self, path: str):
        """
        Carga y normaliza la imagen para inferencia.
        STUB: retorna la ruta sin procesar.
        Implementación completa en sprint de IA:
            import cv2
            img = cv2.imread(path)
            img = cv2.resize(img, (640, 640))
            return img
        """
        return path

    def _inferir(self, imagen):
        """
        Ejecuta el modelo sobre la imagen preprocesada.
        STUB: retorna resultados vacíos.
        """
        return {}

    def _postprocesar(self, resultados: dict) -> dict:
        """
        Traduce la salida del modelo al formato estándar del sistema.
        STUB: retorna diagnóstico neutro.
        """
        return {
            'tipo_piel_detectado': None,
            'nivel_acne':    'ninguno',
            'nivel_manchas': 'ninguno',
            'nivel_arrugas': 'ninguno',
            'nivel_poros':   'ninguno',
            'nivel_brillo':  'ninguno',
            'nivel_ojeras':  'ninguno',
            'observaciones': 'Análisis pendiente — modelo de IA no cargado.',
        }
