import base64
from uuid import uuid4
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from hackathon.models.team import Team, Images
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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        image_file = request.FILES.get("photo")

        if image_file:
            image_base64 = base64.b64encode(image_file.read()).decode("utf-8")

            image_data = Images.objects.create(photo_base64=image_base64)

            team_data = Team.objects.create(
                name=serializer.validated_data["name"],
                edition=serializer.validated_data["edition"],
                leader=serializer.validated_data["leader"],
                verification_token=str(uuid4()),
                photo_base64_team=image_data,
                project=serializer.validated_data["project"],
                valid_registration=serializer.validated_data["valid_registration"],
            )
        else:
            team_data = Team.objects.create(
                name=serializer.validated_data["name"],
                edition=serializer.validated_data["edition"],
                leader=serializer.validated_data["leader"],
                verification_token=str(uuid4()),
                project=serializer.validated_data["project"],
                valid_registration=serializer.validated_data["valid_registration"],
            )
        
        students = serializer.validated_data["students"]
        team_data.students.set(students)

        output_serializer_edition = TeamListSerializer(team_data)
        return Response(output_serializer_edition.data, status=status.HTTP_201_CREATED)

    http_method_names = ["get", "post", "patch", "delete"]
