from hackathon.models import Avaliation, Ranking

def update_rankings(avaliation_id):
    avaliation_instance = Avaliation.objects.get(id=avaliation_id)

    ranking = Ranking.objects.get(team=avaliation_instance.team)
    all_edition_rankings = Ranking.objects.filter(edition=ranking.edition)
    
    if all_edition_rankings.exists():
        recalculate_rankings(all_edition_rankings)

def get_final_grade(all_team_avaliations):
    return sum([avaliation.grade for avaliation in all_team_avaliations]) / len(all_team_avaliations)

def recalculate_rankings(all_edition_rankings):
    sorted_ranking_grades = sorted([ranking.final_grade for ranking in all_edition_rankings], reverse=True)
    used_ranks = []

    index = 1

    for ranking in sorted_ranking_grades:
        ranks = all_edition_rankings.filter(final_grade=ranking)

        if ranking in used_ranks:
            continue

        if len(ranks) == 1:
            rank = ranks.first()
            rank.classification = index
            rank.save()
            used_ranks.append(rank.final_grade)
            index += 1
        else:
            for rank in ranks:
                rank.classification = index
                rank.save()
                used_ranks.append(rank.final_grade)

            index += 1