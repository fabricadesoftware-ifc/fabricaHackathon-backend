from rest_framework.serializers import ModelSerializer

from hackathon.models import Edicao, AvaliadorEdicao, EdicaoCriterio

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

class AvaliadorEdicaoSerializer(ModelSerializer):
    class Meta:
        model = AvaliadorEdicao
        fields = '__all__'

class AvaliadorEdicaoDetailSerializer(ModelSerializer):
    class Meta:
        model = AvaliadorEdicao
        fields = '__all__'
        depth = 1

class EdicaoCriterioSerializer(ModelSerializer):
    class Meta:
        model = EdicaoCriterio
        fields = '__all__'

class EdicaoCriterioDetailSerializer(ModelSerializer):
    class Meta:
        model = EdicaoCriterio
        fields = '__all__'
        depth = 1