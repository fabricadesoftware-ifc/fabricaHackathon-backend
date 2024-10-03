import random
from hackathon.models import Criterion, Avaliation, Team
from user.models import CustomUser
from django.contrib.auth.models import Group
from populate.resources.data_avaliation import criteria


def populate_criteria():
    if Criterion.objects.exists():
        return

    criteria_to_insert = [Criterion(**criterion) for criterion in criteria]
    Criterion.objects.bulk_create(criteria_to_insert)


def populate_avaliations():
    if Avaliation.objects.exists():
        return

    teams = list(Team.objects.all())
    criteria = list(Criterion.objects.all())

    avaliators = CustomUser.objects.filter(groups__name="Avaliators")

    avaliations_to_insert = []

    for team in teams:
        for criterion in criteria:
            for avaliator in avaliators:
                avaliations_to_insert.append(
                    Avaliation(
                        team=team,
                        criterion=criterion,
                        avaliator=avaliator,
                        grade=random.randint(0, 10),
                    )
                )

    Avaliation.objects.bulk_create(avaliations_to_insert)
    