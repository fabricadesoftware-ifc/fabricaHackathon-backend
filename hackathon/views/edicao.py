from rest_framework.viewsets import ModelViewSet

from hackathon.models import Edicao, AvaliadorEdicao, EdicaoCriterio
from hackathon.serializers import EdicaoCreateSerializer, EdicaoListSerializer, EdicaoRetrieveSerializer, AvaliadorEdicaoDetailSerializer, AvaliadorEdicaoSerializer, EdicaoCriterioSerializer, EdicaoCriterioDetailSerializer

class EdicaoViewSet(ModelViewSet):
    queryset = Edicao.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return EdicaoListSerializer
        if self.action == 'retrieve':
            return EdicaoRetrieveSerializer
        return EdicaoCreateSerializer
    
class AvaliadorEdicaoViewSet(ModelViewSet):
    queryset = AvaliadorEdicao.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return AvaliadorEdicaoDetailSerializer
        return AvaliadorEdicaoSerializer

class EdicaoCriterioViewSet(ModelViewSet):
    queryset = EdicaoCriterio.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return EdicaoCriterioDetailSerializer
        return EdicaoCriterioSerializer