from rest_framework.serializers import ModelSerializer

from hackathon.models import Avaliador

class AvaliadorListSerializer(ModelSerializer):
    class Meta:
        model = Avaliador
        fields = ('id', 'nome', 'github')

class AvaliadorSerializer(ModelSerializer):
    class Meta:
        model = Avaliador
        fields = '__all__'