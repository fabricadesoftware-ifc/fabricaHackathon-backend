from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import ModelSerializer
from .models import CustomUser, StudentProfile

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        # Add any other fields you want in the token
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
