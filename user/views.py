from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
from rest_framework.viewsets import ModelViewSet
from .models import CustomUser, StudentProfile
from .serializers import UserSerializer, UserDetailSerializer, StudentProfileCreateSerializer, StudentProfileDetailSerializer, StudentProfileListSerializer
from .filters import UserFilter

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    filterset_class = UserFilter

    def get_serializer_class(self):
        if self.action in ['retrieve']:
            return UserDetailSerializer
        return UserSerializer

class StudentProfileViewSet(ModelViewSet):
    queryset = StudentProfile.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return StudentProfileDetailSerializer
        elif self.action == 'list':
            return StudentProfileListSerializer
        else:
            return StudentProfileCreateSerializer