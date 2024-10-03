from rest_framework.serializers import ModelSerializer

from hackathon.models import Supporter

class SupporterListSerializer(ModelSerializer):
    class Meta:
        model = Supporter
        fields = ('id', 'company', 'logo', 'link')
        depth = 1

class SupporterRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Supporter
        fields = '__all__'
        depth = 1

class SupporterCreateSerializer(ModelSerializer):
    class Meta:
        model = Supporter
        fields = '__all__'