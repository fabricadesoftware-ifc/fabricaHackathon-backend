from django.dispatch import receiver
from django.db.models.signals import post_save
from hackathon.models import Avaliation
from hackathon.actions import update_rankings

@receiver(post_save, sender=Avaliation)
def handle_grade_change(sender, instance, created, **kwargs):
    update_rankings(instance.id)