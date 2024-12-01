from rest_framework.serializers import ModelSerializer, SlugRelatedField
from django.core.exceptions import ValidationError
from uploader.serializers import ImageSerializer

from hackathon.models import Edition, ClassInfo
from uploader.models import Image


def min_members_is_greater_than_max_members(attrs):
    return attrs["max_members"] <= attrs["min_members"]


def validate_involved_classes(self, value):
    selected_courses = self.initial_data.get("courses")
    valid_classes = ClassInfo.objects.filter(course__in=selected_courses)
    invalid_classes = [cls for cls in value if cls not in valid_classes]

    if invalid_classes:
        raise ValidationError(f"Invalid classes: {invalid_classes}")
    return value


class EditionListSerializer(ModelSerializer):
    photo = ImageSerializer(required=False, read_only=True)

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
            "courses",
            "involved_classes",
            "categories",
            "criteria",
            "avaliators",
            "photo",
        )
        depth = 2


class EditionRetrieveSerializer(ModelSerializer):
    capa = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Edition
        fields = "__all__"
        depth = 2


class EditionWriteSerializer(ModelSerializer):
    photo = SlugRelatedField(
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )

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
        read_only_fields = ("id",)

    def validate(self, attrs):
        if "max_members" in attrs or "min_members" in attrs:
            if min_members_is_greater_than_max_members(attrs):
                raise ValidationError("Min members cannot exceed max members")
        if "involved_classes" in attrs:
            validate_involved_classes(self, attrs["involved_classes"])

        return super().validate(attrs)
