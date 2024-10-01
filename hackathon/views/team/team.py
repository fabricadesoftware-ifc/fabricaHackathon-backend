import base64
from uuid import uuid4
from django.urls import reverse
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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        image_file = request.FILES.get("photo")

        if image_file:
            image_base64 = base64.b64encode(image_file.read()).decode("utf-8")

            image_data = Images.objects.create(photo_base64=image_base64)
            breakpoint()

            team_data = Team.objects.create(
                name=serializer.validated_data["name"],
                edition=serializer.validated_data["edition"],
                deploy_link=serializer.validated_data["deploy_link"],
                repository_link=serializer.validated_data["repository_link"],
                presentation_link=serializer.validated_data["presentation_link"],
                video_link=serializer.validated_data["video_link"],
                pitch_link=serializer.validated_data["pitch_link"],
                leader=serializer.validated_data["leader"],
                category=serializer.validated_data["category"],
                verification_token=str(uuid4()),
                photo_base64_team=image_data,
            )

        students = serializer.validated_data["students"]
        team_data.students.set(students)

        output_serializer_edition = TeamListSerializer(team_data)
        return Response(output_serializer_edition.data, status=status.HTTP_201_CREATED)

    http_method_names = ["get", "post", "patch", "delete"]
