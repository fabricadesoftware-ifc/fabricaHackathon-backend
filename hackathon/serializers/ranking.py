from rest_framework import serializers
from hackathon.serializers.team import TeamListSerializer

from hackathon.models import Ranking

class RankingSerializer(serializers.ModelSerializer):
    team = TeamListSerializer()
    class Meta:
        model = Ranking
        fields =  '__all__'

class RankingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ranking
        fields =  '__all__'
        depth = 2
