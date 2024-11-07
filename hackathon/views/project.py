from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from hackathon.models import Project
from hackathon.serializers import ProjectListSerializer, ProjectDetailSerializer, ProjectCreateSerializer

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ProjectListSerializer
        if self.action == "retrieve":
            return ProjectDetailSerializer
        return ProjectCreateSerializer