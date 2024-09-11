import random
from hackathon.models import Criterion, Avaliation, Team, Avaliator, Ranking, Edition
from hackathon.resources.data_avaliation import criteria


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
    avaliators = list(Avaliator.objects.all())

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

def populate_rankings():
    if Ranking.objects.exists():
        return
    
    teams = list(Team.objects.all())
    editions = list(Edition.objects.all())

    rankings_to_insert = []

    for team in teams:
        final_grade = sum([avaliation.grade for avaliation in Avaliation.objects.filter(team=team)]) / len(Avaliation.objects.filter(team=team))

        ranking = Ranking(
            team=team,
            final_grade=final_grade,
            classification=1,
            edition=team.edition
        )
        rankings_to_insert.append(ranking)

    for edition in editions:
        edition_rankings = filter(lambda ranking: ranking.edition == edition, rankings_to_insert)

        for index, ranking in enumerate(edition_rankings):
            for other_ranking in edition_rankings:
                if ranking.final_grade < other_ranking.final_grade:
                    ranking.classification += 1
        
    Ranking.objects.bulk_create(rankings_to_insert)