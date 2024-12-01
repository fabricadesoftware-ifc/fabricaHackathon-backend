from uuid import uuid4
from rest_framework.viewsets import ModelViewSet

from hackathon.models.team import Team
from hackathon.serializers.team import (
    TeamRetrieveSerializer,
    TeamListSerializer,
    TeamCreateSerializer,
    TeamUpdateSerializer,
)

from hackathon.filters.team import TeamFilter


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    filterset_class = TeamFilter

    def get_serializer_class(self):
        if self.action == "list":
            return TeamListSerializer
        if self.action == "retrieve":
            return TeamRetrieveSerializer
        if self.action in ["update", "partial_update"]:
            return TeamUpdateSerializer
        return TeamCreateSerializer

    http_method_names = ["get", "post", "patch", "delete"]
