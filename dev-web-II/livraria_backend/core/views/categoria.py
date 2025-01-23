from rest_framework.viewsets import ModelViewSet
from core.models import Categoria
from core.serializers import CategoriaSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["descricao"]
    search_fields = ["descricao"]
    ordering_fields = ["descricao", "id"]
    ordering = ["descricao"]
