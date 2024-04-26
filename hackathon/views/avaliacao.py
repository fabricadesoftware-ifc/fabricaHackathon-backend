from rest_framework.viewsets import ModelViewSet

from hackathon.models import Avaliacao
from hackathon.serializers import AvaliacaoSerializer, AvaliacaoDetailSerializer

class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return AvaliacaoDetailSerializer
        return AvaliacaoSerializer