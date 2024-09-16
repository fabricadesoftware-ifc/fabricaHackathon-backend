from django.dispatch import receiver
from django.db.models.signals import post_save
from hackathon.tasks import send_new_team_request_email_to_teachers
from hackathon.models import Team
from django.urls import reverse
from uuid import uuid4


@receiver(post_save, sender=Team)
def handle_new_team_request(sender, instance, created, **kwargs):
    if created:
        token: str = str(uuid4())
        instance.verification_token = token
        instance.save()

        accept_team_path = reverse("accept-team", kwargs={"verification_token": token})
        accept_team_link = f"http://localhost:8000{accept_team_path}"

        reject_team_path = reverse("reject-team", kwargs={"verification_token": token})
        reject_team_link = f"http://localhost:8000/{reject_team_path}"

        print(instance.id, accept_team_link, reject_team_link)

        send_new_team_request_email_to_teachers.delay(
            instance.id, accept_team_link, reject_team_link
        )
