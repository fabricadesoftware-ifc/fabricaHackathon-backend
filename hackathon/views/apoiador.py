from rest_framework.viewsets import ModelViewSet

from hackathon.models import Apoiador
from hackathon.serializers import ApoiadorListSerializer, ApoiadorCreateSerializer, ApoiadorRetrieveSerializer

class ApoiadorViewSet(ModelViewSet):
    queryset = Apoiador.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ApoiadorRetrieveSerializer
        elif self.action == 'create':
            return ApoiadorCreateSerializer
        return ApoiadorListSerializer