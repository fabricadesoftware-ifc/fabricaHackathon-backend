from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from hackathon.models import Edition, Student, Team
from hackathon.serializers import StudentListSerializer
from hackathon.filters import StudentFilter

def get_available_students(edition):
    unavailable_student_ids = Team.objects.filter(
        edition=edition
    ).values_list("students", flat=True).distinct()

    available_students = Student.objects.exclude(id__in=unavailable_student_ids).filter(class_info__in=edition.involved_classes.all())

    return available_students


class AvailableStudentViewSet(ViewSet):
    filterset_class = StudentFilter
    @action(detail=False, methods=["get"], url_path="edition/(?P<edition_id>\d+)")
    def available_students(self, request, edition_id=None):
        edition = get_object_or_404(Edition, id=edition_id)
        available_students = get_available_students(edition)

        filtered_students = self.filterset_class(request.GET, queryset=available_students).qs

        serializer = StudentListSerializer(filtered_students, many=True)
        return Response(serializer.data)
