from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import permission_classes
from ..permissions import IsAuthenticatedOrReadOnly

from hackathon.models import Avaliation
from hackathon.serializers import AvaliationSerializer, AvaliationDetailSerializer

@permission_classes([IsAuthenticatedOrReadOnly])
class FreeAvaliationViewSet(ModelViewSet):
    queryset = Avaliation.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return AvaliationDetailSerializer
        return AvaliationSerializer