import random
from hackathon.models import Criterion, Avaliation, Team
from user.models import CustomUser
from django.contrib.auth.models import Group


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
                        grade=round(random.uniform(0, 10), 2)
                    )
                )

    Avaliation.objects.bulk_create(avaliations_to_insert)
