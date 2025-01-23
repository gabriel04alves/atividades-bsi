from rest_framework.viewsets import ModelViewSet
from core.models import Autor
from core.serializers import AutorSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["nome"]
    search_fields = ["nome"]
    ordering_fields = ["nome", "email"]
    ordering = ["nome"]
