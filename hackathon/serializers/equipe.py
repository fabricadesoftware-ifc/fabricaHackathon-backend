from rest_framework.serializers import ModelSerializer

from hackathon.models import Equipe

class EquipeListSerializer(ModelSerializer):
    class Meta:
        model = Equipe
        fields = ('id', 'nome', 'edicao', 'foto_equipe')

class EquipeRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Equipe
        fields = '__all__'
        depth = 1

class EquipeCreateSerializer(ModelSerializer):
    class Meta:
        model = Equipe
        fields = '__all__'