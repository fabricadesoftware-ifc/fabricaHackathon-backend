from rest_framework.viewsets import ModelViewSet

from hackathon.models import Ranking
from hackathon.serializers import RankingDetailSerializer, RankingSerializer
from hackathon.filters import RankingFilter

class RankingViewSet(ModelViewSet):
    queryset = Ranking.objects.all()
    filterset_class=RankingFilter

    def get_serializer_class(self):
        if self.action == "retrieve":
            return RankingDetailSerializer
        return RankingSerializer