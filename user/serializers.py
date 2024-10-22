from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import ModelSerializer
from .models import CustomUser, StudentProfile

def get_user_type(user):
    teacher_group = user.groups.filter(name="Teachers").exists()
    student_group = user.groups.filter(name="Students").exists()
    avaliator_group = user.groups.filter(name="Avaliators").exists()
    if teacher_group:
        return "teacher"
    elif student_group:
        return "student"
    elif avaliator_group:
        return "avaliator"

def get_student_profile_id(user):
    if user.has_student_profile():
        return user.student_profile.id
    else:
        return None

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['name'] = user.name
        token['email'] = user.email
        token['user_type'] = get_user_type(user)
        token['student_profile_id'] = get_student_profile_id(user)
        return token

class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "email",
            "name",
        ]

    def Create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
        depth = 1

class StudentProfileSerializer(ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = "__all__"
