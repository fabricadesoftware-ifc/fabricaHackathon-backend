from rest_framework.viewsets import ModelViewSet

from hackathon.models import Turma
from hackathon.serializers import TurmaDetailSerializer, TurmaSerializer

class TurmaViewSet(ModelViewSet):
    queryset = Turma.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return TurmaDetailSerializer
        return TurmaSerializer