from django_filters.rest_framework import FilterSet, CharFilter, NumberFilter

from hackathon.models import Student

class StudentFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    class_info = NumberFilter(field_name='class_info__id')

    class Meta:
        model = Student
        fields = ['name', 'class_info']