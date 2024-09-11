from hackathon.models import Avaliation, Ranking

def update_rankings(avaliation_id):
    avaliation_instance = Avaliation.objects.get(id=avaliation_id)
    all_team_avaliations = Avaliation.objects.filter(team=avaliation_instance.team)
    all_edition_avaliations = Avaliation.objects.filter(team__edition=avaliation_instance.team.edition)

    ranking = Ranking.objects.get(team=avaliation_instance.team)
    all_edition_rankings = Ranking.objects.filter(edition=ranking.edition)

    ranking.final_grade = get_final_grade(all_team_avaliations)
    
    if all_edition_rankings.exists():
        recalculate_rankings(all_edition_rankings, ranking)
    else:
        rankings_to_create = []
        for avaliation in all_edition_avaliations:
            ranking = Ranking(
                team=avaliation.team,
                final_grade=get_final_grade(Avaliation.objects.filter(team=avaliation.team)),
                classification=1,
                edition=avaliation.team.edition
            )
            rankings_to_create.append(ranking)
        
        Ranking.objects.bulk_create(rankings_to_create)
        recalculate_rankings(all_edition_rankings, ranking)

def get_final_grade(all_team_avaliations):
    return sum([avaliation.grade for avaliation in all_team_avaliations]) / len(all_team_avaliations)

def recalculate_rankings(all_edition_rankings, ranking):
    for rank in all_edition_rankings:
            if rank.final_grade < ranking.final_grade:
                rank.classification += 1
                rank.save()

    ranking.save()