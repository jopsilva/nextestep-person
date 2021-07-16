from person.models import Type
from person.serializer import TypeSerializar
from rest_framework import viewsets

class TypeViewSets(viewsets.ModelViewSet):
    """Exibindo tipos de Pessoas"""
    queryset = Type.objects.all()
    serializer_class = TypeSerializar