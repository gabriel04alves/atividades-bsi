from rest_framework.viewsets import ModelViewSet
from core.models import Categoria, Editora
from core.serializers import CategoriaSerializer, EditoraSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["nome"]
    search_fields = ["nome"]
