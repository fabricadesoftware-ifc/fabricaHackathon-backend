from rest_framework.serializers import ModelSerializer

from hackathon.models import Criterion

class CriterionListSerializer(ModelSerializer):
    class Meta:
        model = Criterion
        fields = ('id', 'description', 'weight')

class CriterionSerializer(ModelSerializer):
    class Meta:
        model = Criterion
        fields = '__all__'