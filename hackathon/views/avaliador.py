from rest_framework.viewsets import ModelViewSet

from hackathon.models import Avaliador
from hackathon.serializers import AvaliadorSerializer, AvaliadorListSerializer

class AvaliadorViewSet(ModelViewSet):
    queryset = Avaliador.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return AvaliadorListSerializer
        return AvaliadorSerializer