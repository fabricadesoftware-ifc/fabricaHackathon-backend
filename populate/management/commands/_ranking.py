from hackathon.models import Team, Ranking, Edition, Avaliation


def populate_rankings():
    if Ranking.objects.exists():
        return

    teams = list(Team.objects.all())
    editions = list(Edition.objects.all())

    rankings_to_insert = []

    for team in teams:
        if len(Avaliation.objects.filter(team=team)) != 0:
            final_grade = sum(
                [avaliation.grade for avaliation in Avaliation.objects.filter(team=team)]
            ) / len(Avaliation.objects.filter(team=team))

            ranking = Ranking(
                team=team, final_grade=final_grade, classification=1, edition=team.edition
            )
            rankings_to_insert.append(ranking)

    for edition in editions:
        edition_rankings = filter(
            lambda ranking: ranking.edition == edition, rankings_to_insert
        )

        for index, ranking in enumerate(edition_rankings):
            for other_ranking in edition_rankings:
                if ranking.final_grade < other_ranking.final_grade:
                    ranking.classification += 1

    Ranking.objects.bulk_create(rankings_to_insert)
