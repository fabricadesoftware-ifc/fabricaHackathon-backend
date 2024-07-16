from rest_framework.serializers import ModelSerializer

from hackathon.models import Avaliation

class AvaliationSerializer(ModelSerializer):
    class Meta:
        model = Avaliation
        fields = '__all__'

class AvaliationDetailSerializer(ModelSerializer):
    class Meta:
        model = Avaliation
        fields = '__all__'
        depth = 1