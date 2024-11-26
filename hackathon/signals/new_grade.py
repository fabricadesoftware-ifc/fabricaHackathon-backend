from django.dispatch import receiver
from django.db.models.signals import post_save
from hackathon.models import Avaliation, Ranking
from hackathon.actions import update_rankings, get_final_grade

@receiver(post_save, sender=Avaliation)
def handle_grade_change(sender, instance, created, **kwargs):
    ranking = Ranking.objects.filter(team=instance.team, edition=instance.team.edition).first()
    if ranking is None:
      final_grade = get_final_grade(Avaliation.objects.filter(team=instance.team))
      ranking = Ranking(team=instance.team, final_grade=final_grade, classification=0, edition=instance.team.edition)
      ranking.save()
      update_rankings(instance.id)
    else:
      ranking.final_grade = get_final_grade(Avaliation.objects.filter(team=instance.team))
      ranking.save()
      update_rankings(instance.id)
