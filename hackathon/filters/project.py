from django_filters.rest_framework import FilterSet, CharFilter

from hackathon.models import Project

class ProjectFilter(FilterSet):
  edition_id = CharFilter(field_name='team_id__edition__id', lookup_expr='exact')

  class Meta:
    model = Project
    fields = ['edition_id']
