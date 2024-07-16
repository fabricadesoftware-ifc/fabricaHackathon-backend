from rest_framework.serializers import ModelSerializer

from hackathon.models import Edition

class EditionListSerializer(ModelSerializer):
    class Meta:
        model = Edition
        fields = ('id', 'year', 'edition_photo', 'applications_accepted', 'registration_deadline')

class EditionRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Edition
        fields = '__all__'
        depth = 1

class EditionCreateSerializer(ModelSerializer):
    class Meta:
        model = Edition
        fields = '__all__'