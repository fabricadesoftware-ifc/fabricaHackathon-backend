from rest_framework.serializers import ModelSerializer

from hackathon.models import Team

class TeamListSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name', 'edition', 'photo_team')

class TeamRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        depth = 1

class TeamCreateSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'