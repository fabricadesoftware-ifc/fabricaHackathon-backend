from rest_framework.serializers import ModelSerializer

from hackathon.models import class_info

class ClassInfoSerializer(ModelSerializer):
    class Meta:
        model = class_info
        fields = '__all__'

class ClassInfoDetailSerializer(ModelSerializer):
    class Meta:
        model = class_info
        fields =  '__all__'
        depth = 1