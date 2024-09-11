from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from hackathon.models import Edition
from hackathon.serializers import EditionWriteSerializer, EditionListSerializer, EditionRetrieveSerializer
from hackathon.signals import applications_accepted_changed

class EditionViewSet(ModelViewSet):
    queryset = Edition.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return EditionListSerializer
        if self.action == 'retrieve':
            return EditionRetrieveSerializer
        return EditionWriteSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
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
                new_value=new_value
            )

        return Response(serializer.data)
