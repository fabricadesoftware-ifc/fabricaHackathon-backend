from rest_framework.viewsets import ModelViewSet

from hackathon.models import Course
from hackathon.serializers import CourseListSerializer, CourseSerializer

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CourseListSerializer
        return CourseSerializer