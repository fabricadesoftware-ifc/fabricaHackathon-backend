from rest_framework.serializers import ModelSerializer

from hackathon.models import Avaliator

class AvaliatorListSerializer(ModelSerializer):
    class Meta:
        model = Avaliator
        fields = ('id', 'name', 'github')

class AvaliatorSerializer(ModelSerializer):
    class Meta:
        model = Avaliator
        fields = '__all__'