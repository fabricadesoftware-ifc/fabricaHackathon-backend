from rest_framework.serializers import ModelSerializer

from hackathon.models import Apoiador

class ApoiadorListSerializer(ModelSerializer):
    class Meta:
        model = Apoiador
        fields = ('id', 'empresa', 'logo', 'link', 'edicao')
        depth = 1

class ApoiadorRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Apoiador
        fields = '__all__'
        depth = 1

class ApoiadorCreateSerializer(ModelSerializer):
    class Meta:
        model = Apoiador
        fields = '__all__'