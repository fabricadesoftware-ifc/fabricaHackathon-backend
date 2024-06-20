from rest_framework.serializers import ModelSerializer

from hackathon.models import Edicao

class EdicaoListSerializer(ModelSerializer):
    class Meta:
        model = Edicao
        fields = ('id', 'ano', 'foto_edicao', 'aceita_inscricoes', 'prazo_inscricoes')

class EdicaoRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Edicao
        fields = '__all__'
        depth = 1

class EdicaoCreateSerializer(ModelSerializer):
    class Meta:
        model = Edicao
        fields = '__all__'