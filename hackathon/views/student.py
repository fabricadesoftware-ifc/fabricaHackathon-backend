from rest_framework.viewsets import ModelViewSet

from hackathon.models import Student
from hackathon.serializers import StudentCreateSerializer, StudentRetrieveSerializer, StudentListSerializer
from hackathon.filters import StudentFilter

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    filterset_class = StudentFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return StudentListSerializer
        if self.action == 'retrieve':
            return StudentRetrieveSerializer
        return StudentCreateSerializer