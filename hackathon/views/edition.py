from rest_framework.viewsets import ModelViewSet

from hackathon.models import Edition
from hackathon.serializers import EditionCreateSerializer, EditionListSerializer, EditionRetrieveSerializer

class EditionViewSet(ModelViewSet):
    queryset = Edition.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return EditionListSerializer
        if self.action == 'retrieve':
            return EditionRetrieveSerializer
        return EditionCreateSerializer