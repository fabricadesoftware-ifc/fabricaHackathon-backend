from rest_framework.viewsets import ModelViewSet

from hackathon.models import Edicao
from hackathon.serializers import EdicaoCreateSerializer, EdicaoListSerializer, EdicaoRetrieveSerializer

class EdicaoViewSet(ModelViewSet):
    queryset = Edicao.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return EdicaoListSerializer
        if self.action == 'retrieve':
            return EdicaoRetrieveSerializer
        return EdicaoCreateSerializer