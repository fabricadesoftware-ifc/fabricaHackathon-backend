from rest_framework.serializers import ModelSerializer

from hackathon.models import ClassInfo

class ClassInfoSerializer(ModelSerializer):
    class Meta:
        model = ClassInfo
        fields = '__all__'

class ClassInfoDetailSerializer(ModelSerializer):
    class Meta:
        model = ClassInfo
        fields =  '__all__'
        depth = 1