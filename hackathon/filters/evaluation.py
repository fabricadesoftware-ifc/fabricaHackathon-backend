from django_filters.rest_framework import FilterSet, CharFilter

from hackathon.models import Avaliation

class EvaluationFilter(FilterSet):
  team_id = CharFilter(field_name='team__id', lookup_expr='exact')
  evaluator_id = CharFilter(field_name='avaliator__id', lookup_expr='exact')

  class Meta:
    model = Avaliation
    fields = ['team_id', 'evaluator_id']
