import base64
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from hackathon.models import Edition
from hackathon.serializers import (
    EditionWriteSerializer,
    EditionListSerializer,
    EditionRetrieveSerializer,
)
from hackathon.signals import applications_accepted_changed


class EditionViewSet(ModelViewSet):
    queryset = Edition.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return EditionListSerializer
        if self.action == "retrieve":
            return EditionRetrieveSerializer
        return EditionWriteSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        photo_change = serializer.validated_data["photo"]
        image_base64 = base64.b64encode(photo_change.read()).decode("utf-8")

        edition_data = Edition.objects.create(
            year=serializer.validated_data["year"],
            semester=serializer.validated_data["semester"],
            edition_photo_base64=image_base64,
            applications_accepted=serializer.validated_data["applications_accepted"],
            registration_deadline=serializer.validated_data["registration_deadline"],
            start_date=serializer.validated_data["start_date"],
            finish_date=serializer.validated_data["finish_date"],
            min_members=serializer.validated_data["min_members"],
            max_members=serializer.validated_data["max_members"],
        )

        output_serializer = EditionListSerializer(edition_data)

        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        old_value = instance.applications_accepted

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        new_value = instance.applications_accepted

        if new_value != old_value:
            applications_accepted_changed.send(
                sender=Edition,
                instance=instance,
                old_value=old_value,
                new_value=new_value,
            )

        return Response(serializer.data)
