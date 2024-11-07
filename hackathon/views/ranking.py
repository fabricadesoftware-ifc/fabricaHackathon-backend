from rest_framework.viewsets import ModelViewSet

from hackathon.models import Ranking
from hackathon.serializers import RankingDetailSerializer, RankingSerializer
from hackathon.filters import RankingFilter
from hackathon.models import Edition
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class RankingViewSet(ModelViewSet):
    queryset = Ranking.objects.all()
    filterset_class=RankingFilter

    @action(detail=False, methods=["get"], url_path="edition/(?P<edition_id>\d+)")
    def ranking(self, request, edition_id=None):
        edition = get_object_or_404(Edition, id=edition_id)
        ranking = Ranking.objects.filter(edition=edition)

        serializer = RankingDetailSerializer(ranking, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return RankingDetailSerializer
        return RankingSerializer
