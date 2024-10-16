from django_filters.rest_framework import FilterSet, CharFilter, BooleanFilter

from hackathon.models import Team

class TeamFilter(FilterSet):
    student_id = CharFilter(field_name='students', lookup_expr='exact')
    student_name = CharFilter(field_name='students__user__name', lookup_expr='icontains')
    student_email = CharFilter(field_name='students__user__email', lookup_expr='icontains')
    edition_id = CharFilter(field_name='edition', lookup_expr='exact')
    category_id = CharFilter(field_name='category', lookup_expr='exact')

    class Meta:
        model = Team
        fields = ['student_id', 'student_name', 'student_email', 'edition_id', 'category_id']