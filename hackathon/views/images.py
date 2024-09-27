import base64
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from hackathon.models import Images
from hackathon.serializers import ImagesListSerializer, ImagesWriteSerializer


class ImagesViewSet(ModelViewSet):
    queryset = Images.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ImagesListSerializer
        return ImagesWriteSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        photo_change = serializer.validated_data["photo"]
        image_base64 = base64.b64encode(photo_change.read()).decode("utf-8")

        image_data = Images.objects.create(
            photo_base64=image_base64, description=serializer.validated_data["description"]
        )

        output_serializer = ImagesListSerializer(image_data)

        return Response(output_serializer.data, status=status.HTTP_201_CREATED)
