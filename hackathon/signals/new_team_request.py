from django.dispatch import receiver
from django.db.models.signals import post_save
from hackathon.tasks import send_new_team_request_email_to_teachers
from hackathon.models import Team

@receiver(post_save, sender=Team)
def handle_new_team_request(sender, instance, created, **kwargs):
    if created:
        send_new_team_request_email_to_teachers.delay(instance.id)