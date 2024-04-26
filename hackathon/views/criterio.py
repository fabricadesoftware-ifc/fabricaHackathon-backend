from rest_framework.viewsets import ModelViewSet

from hackathon.models import Criterio
from hackathon.serializers import CriterioSerializer, CriterioListSerializer

class CriterioViewSet(ModelViewSet):
    queryset = Criterio.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CriterioListSerializer
        return CriterioSerializer