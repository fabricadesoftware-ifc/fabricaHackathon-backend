from rest_framework.serializers import ModelSerializer

from hackathon.models import Project

class ProjectListSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'category')

class ProjectDetailSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectCreateSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'