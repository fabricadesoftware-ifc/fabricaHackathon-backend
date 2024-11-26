import base64
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from hackathon.models import Project, Images, Team, Category
from hackathon.serializers import (
    ProjectListSerializer,
    ProjectDetailSerializer,
    ProjectCreateSerializer
)
from hackathon.filters import ProjectFilter

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    filterset_class = ProjectFilter

    def get_serializer_class(self):
        if self.action == "list":
            return ProjectListSerializer
        if self.action == "retrieve":
            return ProjectDetailSerializer
        return ProjectCreateSerializer

    def create(self, request, *args, **kwargs):
        # Recupera os dados da requisição
        name = request.data.get("name")
        deploy_link = request.data.get("deploy_link")
        repository_link = request.data.get("repository_link")
        presentation_link = request.data.get("presentation_link")
        video_link = request.data.get("video_link")
        pitch_link = request.data.get("pitch_link")
        category_id = request.data.get("category")
        team_id = request.data.get("team_id")
        description = request.data.get("description")

        image_file = request.FILES.get("photo_file")
        if image_file:
            image_base64 = base64.b64encode(image_file.read()).decode("utf-8")
            image_data = Images.objects.create(photo_base64=image_base64)
        else:
            return Response(
                {"error": "No image provided"}, status=status.HTTP_400_BAD_REQUEST
            )

        category = Category.objects.get(id=category_id) if category_id else None
        team = Team.objects.get(id=team_id) if team_id else None

        project_data = Project.objects.create(
            name=name,
            deploy_link=deploy_link,
            repository_link=repository_link,
            presentation_link=presentation_link,
            video_link=video_link,
            pitch_link=pitch_link,
            category=category,
            project_photo_base64=image_data,
            team_id=team,
            description=description,
        )

        # Serializa o objeto Project criado
        output_serializer_project = ProjectListSerializer(project_data)
        return Response(output_serializer_project.data, status=status.HTTP_201_CREATED)
