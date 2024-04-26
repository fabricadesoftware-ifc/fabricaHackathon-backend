from rest_framework.serializers import ModelSerializer

from hackathon.models import Aluno

class AlunoListSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = ('id', 'nome', 'turma')
        depth = 1

class AlunoRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'
        depth = 1

class AlunoCreateSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'