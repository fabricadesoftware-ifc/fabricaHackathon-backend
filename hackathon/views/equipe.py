from rest_framework.viewsets import ModelViewSet

from hackathon.models import Equipe
from hackathon.serializers import EquipeListSerializer, EquipeRetrieveSerializer, EquipeCreateSerializer

class EquipeViewSet(ModelViewSet):
    queryset = Equipe.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return EquipeListSerializer
        if self.action == 'retrieve':
            return EquipeRetrieveSerializer
        return EquipeCreateSerializer