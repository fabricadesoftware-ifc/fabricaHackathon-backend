from rest_framework.serializers import ModelSerializer

from hackathon.models import Course

class CourseListSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'course_level')

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'