from rest_framework.serializers import ModelSerializer

from hackathon.models import Avaliation, Ranking
from hackathon.actions.rankings import recalculate_rankings

class AvaliationSerializer(ModelSerializer):
    class Meta:
        model = Avaliation
        fields = '__all__'

class AvaliationDetailSerializer(ModelSerializer):
    class Meta:
        model = Avaliation
        fields = '__all__'
        depth = 1
