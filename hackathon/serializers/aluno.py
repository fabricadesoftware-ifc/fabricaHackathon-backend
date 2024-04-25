from rest_framework.serializers import ModelSerializer

from hackathon.models import Aluno

class AlunoListSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = ('id', 'nome', 'turma')

class AlunoDetailSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'