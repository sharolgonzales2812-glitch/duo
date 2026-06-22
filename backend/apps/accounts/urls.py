"""
urls.py — App accounts
Prefijo base: /api/accounts/
"""

from django.urls import path
from . import views

urlpatterns = [
    path('registro/',      views.RegisterView.as_view(),     name='accounts-registro'),
    path('perfil/',        views.PerfilView.as_view(),        name='accounts-perfil'),
    path('cuestionario/',  views.CuestionarioView.as_view(),  name='accounts-cuestionario'),
]
