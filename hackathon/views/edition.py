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
from rest_framework.decorators import action
from datetime import datetime


class EditionViewSet(ModelViewSet):
    queryset = Edition.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return EditionListSerializer
        if self.action == "retrieve":
            return EditionRetrieveSerializer
        return EditionWriteSerializer

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

    @action(
        detail=False, methods=["get"], url_path="avaliator/(?P<evaluator_id>[^/.]+)"
    )
    def evaluator(self, request, evaluator_id=None):
        try:
            editions = self.queryset.filter(avaliators__id=evaluator_id)
            serializer = EditionListSerializer(editions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": f"An error occurred: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    @action(
        detail=False,
        methods=["get"],
        url_path="avaliator/(?P<evaluator_id>[^/.]+)/active",
    )
    def evaluator_active(self, request, evaluator_id=None):
        try:
            editions = self.queryset.filter(
                avaliators__id=evaluator_id,
                finish_date__gte=datetime.now().date(),
            )
            serializer = EditionListSerializer(editions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": f"An error occurred: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )
