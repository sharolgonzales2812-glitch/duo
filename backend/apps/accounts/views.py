"""
views.py — App accounts
Vistas: RegisterView, PerfilView
"""

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import PerfilPiel
from .serializers import RegistroSerializer, PerfilPielSerializer, UsuarioSerializer


class RegisterView(APIView):
    """
    POST /api/accounts/registro/
    Crea un nuevo usuario. No requiere autenticación.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegistroSerializer(data=request.data)
        if serializer.is_valid():
            usuario = serializer.save()
            return Response(
                {
                    'mensaje': 'Usuario creado correctamente.',
                    'usuario': UsuarioSerializer(usuario).data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PerfilView(APIView):
    """
    GET  /api/accounts/perfil/       → datos del usuario autenticado
    PATCH /api/accounts/perfil/      → actualiza datos del usuario
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UsuarioSerializer(request.user)
        return Response(serializer.data)

    def patch(self, request):
        serializer = UsuarioSerializer(
            request.user,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CuestionarioView(APIView):
    """
    POST /api/accounts/cuestionario/
    Guarda o actualiza el perfil de piel tras el cuestionario inicial.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        perfil, _ = PerfilPiel.objects.get_or_create(usuario=request.user)
        serializer = PerfilPielSerializer(perfil, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['cuestionario_completado'] = True
            serializer.save()
            return Response(
                {'mensaje': 'Cuestionario guardado.', 'perfil': serializer.data},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
