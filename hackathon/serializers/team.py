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


class TeamListSerializer(ModelSerializer):

    class Meta:
        model = Team
        fields = (
            "id",
            "name",
            "edition",
            "valid_registration",
            "category",
            "students",
            "leader",
        )



class TeamRetrieveSerializer(ModelSerializer):
    photo_base64_code = serializers.SerializerMethodField()
    class Meta:
        model = Team
        fields = (
            "id",
            "name",
            "students",
            "edition",
            "deploy_link",
            "repository_link",
            "presentation_link",
            "video_link",
            "pitch_link",
            "leader",
            "category",
            "verification_token",
            "photo_base64_code",
        )
        depth = 1

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
            "deploy_link",
            "repository_link",
            "presentation_link",
            "video_link",
            "pitch_link",
            "leader",
            "category",
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
