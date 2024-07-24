from rest_framework.viewsets import ModelViewSet

from hackathon.models import Avaliator
from hackathon.serializers import AvaliatorSerializer, AvaliatorListSerializer

class AvaliatorViewSet(ModelViewSet):
    queryset = Avaliator.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return AvaliatorListSerializer
        return AvaliatorSerializer