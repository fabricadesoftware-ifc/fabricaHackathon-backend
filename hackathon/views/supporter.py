from rest_framework.viewsets import ModelViewSet

from hackathon.models import Supporter
from hackathon.serializers import SupporterListSerializer, SupporterCreateSerializer, SupporterRetrieveSerializer

class SupporterViewSet(ModelViewSet):
    queryset = Supporter.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SupporterRetrieveSerializer
        elif self.action == 'create':
            return SupporterCreateSerializer
        return SupporterListSerializer