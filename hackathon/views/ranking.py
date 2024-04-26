from rest_framework.viewsets import ModelViewSet

from hackathon.models import Ranking
from hackathon.serializers import RankingDetailSerializer, RankingSerializer

class RankinhViewSet(ModelViewSet):
    queryset = Ranking.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return RankingDetailSerializer
        return RankingSerializer