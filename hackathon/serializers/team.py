from rest_framework.serializers import ModelSerializer

from hackathon.models import Team
from rest_framework.validators import ValidationError
from rest_framework import serializers


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


class TeamListSerializer(serializers.ModelSerializer):
    photo_base64_code = serializers.SerializerMethodField()
    project = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = (
            "id",
            "name",
            "photo_base64_code",
            "edition",
            "valid_registration",
            "students",
            "leader",
            "registration_date",
            "project",
        )
        depth = 1

    def get_photo_base64_code(self, obj):
        if obj.photo_base64_team and hasattr(obj.photo_base64_team, "photo_base64"):
            return obj.photo_base64_team.photo_base64
        return None

    def get_project(self, obj):
        project = obj.project
        if project:
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
                "project_photo_base64_code": project.project_photo_base64.photo_base64
                if project.project_photo_base64 and hasattr(project.project_photo_base64, "photo_base64")
                else None,
            }
        return None

class TeamRetrieveSerializer(ModelSerializer):
    photo_base64_code = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = (
            "id",
            "name",
            "students",
            "edition",
            "leader",
            "verification_token",
            "photo_base64_code",
            "valid_registration",
            "registration_date",
            "project",
        )
        depth = 2

    def get_photo_base64_code(self, obj):
        image = obj.photo_base64_team
        if image:
            return image.photo_base64
        return None


class TeamCreateSerializer(ModelSerializer):
    photo = serializers.ImageField(required=False)

    class Meta:
        model = Team
        fields = (
            "name",
            "students",
            "edition",
            "verification_token",
            "photo",
        )

    def validate(self, attrs):
        validate_team_members(attrs)
        validate_team_name(attrs)
        return attrs


class TeamUpdateSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"
