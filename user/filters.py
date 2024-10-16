from django_filters.rest_framework import (
    FilterSet,
    CharFilter,
    BooleanFilter,
)
from user.models import CustomUser

class UserFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    email = CharFilter(field_name='email', lookup_expr='icontains')
    is_active = BooleanFilter(field_name='is_active')

    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'is_active']

class StudentProfileFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    email = CharFilter(field_name='email', lookup_expr='icontains')
    is_active = BooleanFilter(field_name='is_active')

    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'is_active']