from rest_framework.viewsets import ModelViewSet
from django.urls import reverse
from uuid import uuid4

from hackathon.models.team import Team
from hackathon.serializers.team import (
    TeamRetrieveSerializer,
    TeamListSerializer,
    TeamCreateSerializer,
    TeamUpdateSerializer,
)

from hackathon.signals import new_team_request


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return TeamListSerializer
        if self.action == "retrieve":
            return TeamRetrieveSerializer
        if self.action in ["update", "partial_update"]:
            return TeamUpdateSerializer
        return TeamCreateSerializer

    http_method_names = ["get", "post", "patch", "delete"]
