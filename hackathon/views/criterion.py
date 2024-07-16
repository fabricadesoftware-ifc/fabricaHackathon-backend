from rest_framework.viewsets import ModelViewSet

from hackathon.models import Criterion
from hackathon.serializers import CriterionSerializer, CriterionListSerializer

class CriterionViewSet(ModelViewSet):
    queryset = Criterion.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CriterionListSerializer
        return CriterionSerializer