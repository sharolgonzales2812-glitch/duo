"""
urls.py — Rutas principales del proyecto skincaremaysha.
Cada app expone sus propias URLs bajo el prefijo /api/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)

urlpatterns = [
    # Panel de administración
    path('admin/', admin.site.urls),

    # ── Autenticación JWT ────────────────────────────────────────────────────
    path('api/auth/login/',   TokenObtainPairView.as_view(),  name='token-obtain'),
    path('api/auth/refresh/', TokenRefreshView.as_view(),     name='token-refresh'),
    path('api/auth/logout/',  TokenBlacklistView.as_view(),   name='token-blacklist'),

    # ── Apps del proyecto ────────────────────────────────────────────────────
    path('api/accounts/',        include('apps.accounts.urls')),
    path('api/analisis/',        include('apps.analisis.urls')),
    path('api/recomendaciones/', include('apps.recomendaciones.urls')),
    path('api/productos/',       include('apps.productos.urls')),
    path('api/progreso/',        include('apps.progreso.urls')),
]

# Servir archivos media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
