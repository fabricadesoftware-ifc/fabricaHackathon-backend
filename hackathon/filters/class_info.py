from django_filters.rest_framework import FilterSet, CharFilter

from hackathon.models import ClassInfo

class ClassInfoFilter(FilterSet):
  student_id = CharFilter(field_name='team_id__students__id', lookup_expr='exact')

  class Meta:
    model = Project
    fields = ['edition_id']
