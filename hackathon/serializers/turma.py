from rest_framework.serializers import ModelSerializer

from hackathon.models import Turma

class TurmaSerializer(ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'

class TurmaDetailSerializer(ModelSerializer):
    class Meta:
        model = Turma
        fields =  '__all__'
        depth = 1