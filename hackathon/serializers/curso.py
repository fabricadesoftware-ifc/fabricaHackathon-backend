from rest_framework.serializers import ModelSerializer

from hackathon.models import Curso

class CursoListSerializer(ModelSerializer):
    class Meta:
        model = Curso
        fields = ('id', 'nome', 'nivel_curso')

class CursoDetailSerializer(ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'