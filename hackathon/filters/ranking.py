from django_filters.rest_framework import FilterSet, CharFilter

from hackathon.models import Ranking

class RankingFilter(FilterSet):
    edition_id = CharFilter(field_name='edition', lookup_expr='exact')
    classification = CharFilter(field_name='classification', lookup_expr='exact')
    final_grade_over = CharFilter(field_name='final_grade', lookup_expr='gte')
    final_grade_under = CharFilter(field_name='final_grade', lookup_expr='lte')
    team_id = CharFilter(field_name='team', lookup_expr='exact')
    team_name = CharFilter(field_name='team__name', lookup_expr='icontains')
    category = CharFilter(field_name='team__category', lookup_expr='exact')
 
    class Meta:
        model = Ranking
        fields = ['edition_id', 'classification', 'final_grade_over', 'final_grade_under', 'team_id', 'team_name', 'category']