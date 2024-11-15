from rest_framework.viewsets import ModelViewSet
from hackathon.models import Project
from hackathon.filters import ProjectFilter
from hackathon.serializers import ProjectListSerializer, ProjectDetailSerializer, ProjectCreateSerializer

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    filterset_class = ProjectFilter

    def get_serializer_class(self):
        if self.action == "list":
            return ProjectListSerializer
        if self.action == "retrieve":
            return ProjectDetailSerializer
        return ProjectCreateSerializer
