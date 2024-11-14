from django.db.models import Q
from hackathon.models import Team, Edition, Images, Project
from user.models import StudentProfile
from populate.resources.data_team import teams

from faker import Faker

fake = Faker("pt_BR")


def populate_teams():
    if Team.objects.exists():
        return

    teams_to_insert = []
    photo_base64_team = Images.objects.first()

    for index, team_data in enumerate(teams):
        team = Team(
            name=team_data["name"],
            registration_date=team_data["registration_date"],
            valid_registration=team_data["valid_registration"],
            photo_base64_team=photo_base64_team,
        )

        if index % 2 == 0:
            editions = list(Edition.objects.filter(courses__acronym__in=["MCC", "DCC"]))
            if index < len(editions):
                team.edition = editions[index]
            else:
                team.edition = editions[index % len(editions)]

            team.leader = StudentProfile.objects.filter(
                class_info__course__acronym__in=["MCC", "DCC"]
            ).first()

        else:
            editions = list(
                Edition.objects.filter(courses__acronym__in=["INFO", "BSI"])
            )
            if index <= len(editions):
                team.edition = editions[index]
            else:
                team.edition = editions[index % len(editions)]

            team.leader = StudentProfile.objects.filter(
                class_info__course__acronym__in=["INFO", "BSI"]
            ).first()

        edition_categories = list(team.edition.categories.all())
        if index < len(edition_categories):
            team.category = edition_categories[index]
        else:
            team.category = edition_categories[index % len(edition_categories)]

        teams_to_insert.append(team)

    Team.objects.bulk_create(teams_to_insert)

    created_teams = list(Team.objects.all())
    student_group_one = StudentProfile.objects.filter(
        Q(class_info__course__acronym__in=["MCC", "DCC"])
    )
    student_group_two = StudentProfile.objects.filter(
        Q(class_info__course__acronym__in=["INFO", "BSI"])
    )

    for index, team in enumerate(created_teams):
        team.save()
        if index % 2 == 0:
            team.students.set(student_group_one)
        else:
            team.students.set(student_group_two)
