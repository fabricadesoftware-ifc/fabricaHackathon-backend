from rest_framework.viewsets import ModelViewSet
from hackathon.models.class_info import ClassInfo
from hackathon.serializers import ClassInfoDetailSerializer, ClassInfoSerializer

class ClassInfoViewSet(ModelViewSet):
    queryset = ClassInfo.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ClassInfoDetailSerializer
        return ClassInfoSerializer