from django.dispatch import receiver
from django.db.models.signals import post_save
from hackathon.models import Avaliation, Ranking
from hackathon.actions import update_rankings, get_final_grade

@receiver(post_save, sender=Avaliation)
def handle_grade_change(sender, instance, created, **kwargs):
    print('oi')
    ranking = Ranking.objects.get(team=instance.team)
    ranking.final_grade = get_final_grade(Avaliation.objects.filter(team=instance.team))
    ranking.save()
    update_rankings(instance.id)
