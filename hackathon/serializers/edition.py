from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.core.exceptions import ValidationError

from hackathon.models import Edition, Images


def min_members_is_greater_than_max_members(attrs):
    return attrs["max_members"] <= attrs["min_members"]


class EditionListSerializer(ModelSerializer):
    photo_base64_code = serializers.SerializerMethodField()

    class Meta:
        model = Edition
        fields = (
            "id",
            "year",
            "photo_base64_edition",
            "photo_base64_code",
            "applications_accepted",
            "registration_deadline",
        )

    def get_photo_base64_code(self, obj):
        image = obj.photo_base64_edition
        if image:
            return image.photo_base64
        return None


class EditionRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Edition
        fields = "__all__"
        depth = 1


class EditionWriteSerializer(ModelSerializer):
    photo = serializers.ImageField()

    class Meta:
        model = Edition
        fields = (
            "id",
            "year",
            "semester",
            "applications_accepted",
            "registration_deadline",
            "start_date",
            "finish_date",
            "min_members",
            "max_members",
            "involved_classes",
            "courses",
            "avaliators",
            "criteria",
            "categories",
            "supporters",
            "photo",
        )

    def validate(self, attrs):
        if "max_members" in attrs or "min_members" in attrs:
            if min_members_is_greater_than_max_members(attrs):
                raise ValidationError("Min members cannot exceed max members")
        return super().validate(attrs)
