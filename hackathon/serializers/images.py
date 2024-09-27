from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from hackathon.models import Images

class ImagesListSerializer(ModelSerializer):
    class Meta:
        model = Images
        fields = ('id', 'photo_base64', 'description')

class ImagesWriteSerializer(ModelSerializer):
    photo = serializers.ImageField()

    class Meta:
        model = Images
        fields = ('id', 'photo', 'description')
