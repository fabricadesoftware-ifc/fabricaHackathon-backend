from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import permission_classes
from ..permissions import IsAuthenticatedOrReadOnly

from hackathon.models import Avaliacao
from hackathon.serializers import AvaliacaoSerializer, AvaliacaoDetailSerializer

@permission_classes([IsAuthenticatedOrReadOnly])
class AvaliacaoLivreViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return AvaliacaoDetailSerializer
        return AvaliacaoSerializer