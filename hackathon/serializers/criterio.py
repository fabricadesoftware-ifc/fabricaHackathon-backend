from rest_framework.serializers import ModelSerializer

from hackathon.models import Criterio

class CriterioListSerializer(ModelSerializer):
    class Meta:
        model = Criterio
        fields = ('id', 'descricao', 'peso')

class CriterioDetailSerializer(ModelSerializer):
    class Meta:
        model = Criterio
        fields = '__all__'