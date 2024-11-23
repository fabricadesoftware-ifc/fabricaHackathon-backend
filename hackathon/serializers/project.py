from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from hackathon.models import Project

class ProjectListSerializer(ModelSerializer):
    photo_base64_code = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = "__all__"
        depth = 0

    def get_photo_base64_code(self, obj):
        image = obj.project_photo_base64
        if image:
            return image.photo_base64
        return None

class ProjectDetailSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectCreateSerializer(ModelSerializer):
    photo_file = serializers.ImageField(write_only=True, required=False)
    class Meta:
        model = Project
        fields = '__all__'