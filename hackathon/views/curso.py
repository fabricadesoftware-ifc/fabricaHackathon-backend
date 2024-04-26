from rest_framework.viewsets import ModelViewSet

from hackathon.models import Curso
from hackathon.serializers import CursoDetailSerializer, CursoSerializer

class CursoViewSet(ModelViewSet):
    queryset = Curso.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CursoDetailSerializer
        return CursoSerializer