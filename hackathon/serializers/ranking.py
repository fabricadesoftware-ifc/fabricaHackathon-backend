from rest_framework.serializers import ModelSerializer

from hackathon.models import Ranking

class RankingSerializer(ModelSerializer):
    class Meta:
        model = Ranking
        fields = '__all__'

class RankingDetailSerializer(ModelSerializer):
    class Meta:
        model = Ranking
        fields =  '__all__'
        depth = 1