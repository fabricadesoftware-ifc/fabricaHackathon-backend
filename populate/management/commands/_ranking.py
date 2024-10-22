from hackathon.models import Ranking, Edition, Avaliation
from hackathon.actions.rankings import recalculate_rankings, get_final_grade

def populate_rankings():
    if Ranking.objects.exists():
        return

    avaliations = list(Avaliation.objects.all())

    rankings_to_create = []
    
    for avaliation in avaliations:
            if avaliation.team not in [ranking.team for ranking in rankings_to_create]:
                ranking = Ranking(
                    team=avaliation.team,
                    final_grade=get_final_grade(Avaliation.objects.filter(team=avaliation.team)),
                    classification=1,
                    edition=avaliation.team.edition
                )
                rankings_to_create.append(ranking)
        
    Ranking.objects.bulk_create(rankings_to_create)

    for edition in Edition.objects.all():
        recalculate_rankings(Ranking.objects.filter(edition=edition))
