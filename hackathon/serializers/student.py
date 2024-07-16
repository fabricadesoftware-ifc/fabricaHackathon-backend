from rest_framework.serializers import ModelSerializer

from hackathon.models import Student

class StudentListSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'classe')
        depth = 1

class StudentRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        depth = 1

class StudentCreateSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'