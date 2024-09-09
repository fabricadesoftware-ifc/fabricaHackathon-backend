from hackathon.models import Team, Student, Edition
from hackathon.resources.data_team import teams


def populate_teams():
    if Team.objects.exists():
        return

    teams_to_insert = [Team(**team) for team in teams]

    for index, team in enumerate(teams_to_insert):
        if index % 2 == 0:
            editions = list(Edition.objects.filter(courses__acronym__in=["MCC", "DCC"]))
            if index < len(editions):
                team.edition = editions[index]
            else:
                team.edition = editions[index % len(editions)]

            team.leader = Student.objects.filter(
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

            team.leader = Student.objects.filter(
                class_info__course__acronym__in=["INFO", "BSI"]
            ).first()

    Team.objects.bulk_create(teams_to_insert)

    created_teams = list(Team.objects.all())

    for index, team in enumerate(created_teams):
        if index % 2 == 0:
            team.students.set(
                Student.objects.filter(class_info__course__acronym__in=["MCC", "DCC"])
            )
        else:
            team.students.set(
                Student.objects.filter(class_info__course__acronym__in=["INFO", "BSI"])
            )
