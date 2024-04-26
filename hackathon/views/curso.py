from rest_framework.viewsets import ModelViewSet

from hackathon.models import Curso
from hackathon.serializers import CursoListSerializer, CursoSerializer

class CursoViewSet(ModelViewSet):
    queryset = Curso.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CursoListSerializer
        return CursoSerializer