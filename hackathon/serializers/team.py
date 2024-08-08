from rest_framework.serializers import ModelSerializer

from hackathon.models import Team
from rest_framework.validators import ValidationError
 
def validate_team_members(attrs):
    existing_team_members = []
    teams = Team.objects.filter(edition=attrs['edition'])
    for team in teams:
        for student in attrs['students']:
            if team.students.filter(id=student.id).exists():
                existing_team_members.append(student.name)

    if existing_team_members:
        raise ValidationError(f"Students already in a team for this edition: {', '.join(existing_team_members)}")

def validate_team_name(attrs):
    teams = Team.objects.filter(edition=attrs['edition'])
    
    for team in teams:
        if team.name == attrs['name']:
            raise ValidationError(f"Team name already exists.")


class TeamListSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name', 'edition', 'photo_team')

class TeamRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        depth = 1

class TeamCreateSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

    def validate(self, attrs):
        validate_team_members(attrs)
        validate_team_name(attrs)
        return attrs