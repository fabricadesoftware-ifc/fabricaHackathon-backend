from rest_framework.viewsets import ModelViewSet

from hackathon.models import Category
from hackathon.serializers import CategorySerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer