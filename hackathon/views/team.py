from rest_framework.viewsets import ModelViewSet

from hackathon.models import Team
from hackathon.serializers import TeamListSerializer, TeamRetrieveSerializer, TeamCreateSerializer

class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return TeamListSerializer
        if self.action == 'retrieve':
            return TeamRetrieveSerializer
        return TeamCreateSerializer