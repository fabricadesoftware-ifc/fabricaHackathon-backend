from rest_framework.viewsets import ModelViewSet

from hackathon.models import Aluno
from hackathon.serializers import AlunoCreateSerializer, AlunoRetrieveSerializer, AlunoListSerializer
class AlunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return AlunoListSerializer
        if self.action == 'retrieve':
            return AlunoRetrieveSerializer
        return AlunoCreateSerializer