from rest_framework.serializers import ModelSerializer
from django.core.exceptions import ValidationError

from hackathon.models import Edition


def min_members_is_greater_than_max_members(attrs):
    return attrs["max_members"] <= attrs["min_members"]

class EditionListSerializer(ModelSerializer):
    class Meta:
        model = Edition
        fields = ('id', 'year', 'edition_photo', 'applications_accepted', 'registration_deadline')

class EditionRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Edition
        fields = '__all__'
        depth = 1

class EditionWriteSerializer(ModelSerializer):
    class Meta:
        model = Edition
        fields = '__all__'

    def validate(self, attrs):
        if hasattr(attrs, "max_members") or hasattr(attrs, "min_members"):
            if min_members_is_greater_than_max_members(attrs):
                raise ValidationError("Min members cannot exceed max members")
        return super().validate(attrs)
