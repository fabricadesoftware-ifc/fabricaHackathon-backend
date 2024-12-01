from rest_framework import serializers
from hackathon.models import Team
from rest_framework.validators import ValidationError
from uploader.models import Image
from uploader.serializers import ImageSerializer


def validate_team_members(attrs):
    existing_team_members = []
    teams = Team.objects.filter(edition=attrs["edition"])
    for team in teams:
        for student in attrs["students"]:
            if team.students.filter(id=student.id).exists():
                existing_team_members.append(student.name)

    if existing_team_members:
        raise ValidationError(
            f"Students already in a team for this edition: {', '.join(existing_team_members)}"
        )


def validate_team_name(attrs):
    teams = Team.objects.filter(edition=attrs["edition"])

    for team in teams:
        if team.name == attrs["name"]:
            raise ValidationError(f"Team name already exists.")


# Serializer para listar os times
class TeamListSerializer(serializers.ModelSerializer):
    project = serializers.SerializerMethodField()
    photo = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Team
        fields = (
            "id",
            "name",
            "photo",
            "edition",
            "valid_registration",
            "students",
            "leader",
            "registration_date",
            "project",
        )
        depth = 1

    def get_project(self, obj):
        if hasattr(obj, "project") and obj.project:
            project = obj.project
            return {
                "id": project.id,
                "name": project.name,
                "category": project.category.id if project.category else None,
                "description": project.description,
                "deploy_link": project.deploy_link,
                "repository_link": project.repository_link,
                "presentation_link": project.presentation_link,
                "pitch_link": project.pitch_link,
                "video_link": project.video_link,
                "photo": project.photo,
            }
        return None


class TeamRetrieveSerializer(serializers.ModelSerializer):
    project = serializers.SerializerMethodField()
    photo = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Team
        fields = (
            "id",
            "name",
            "students",
            "edition",
            "leader",
            "verification_token",
            "photo",
            "valid_registration",
            "registration_date",
            "project",
        )
        depth = 2

    def get_project(self, obj):
        if hasattr(obj, "project") and obj.project:
            project = obj.project
            return {
                "id": project.id,
                "name": project.name,
                "category": project.category.id if project.category else None,
                "description": project.description,
                "deploy_link": project.deploy_link,
                "repository_link": project.repository_link,
                "presentation_link": project.presentation_link,
                "pitch_link": project.pitch_link,
                "video_link": project.video_link,
                "photo": project.photo,
            }
        return None


class TeamCreateSerializer(serializers.ModelSerializer):
    photo = serializers.SlugRelatedField(
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )

    class Meta:
        model = Team
        fields = (
            "name",
            "students",
            "edition",
            "leader",
            "verification_token",
            "photo",
        )

    def validate(self, attrs):
        validate_team_members(attrs)
        validate_team_name(attrs)
        return attrs


class TeamUpdateSerializer(serializers.ModelSerializer):
    photo = serializers.SlugRelatedField(
        source="photo",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )

    class Meta:
        model = Team
        fields = "__all__"
