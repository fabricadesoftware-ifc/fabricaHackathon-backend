from celery import shared_task
from django.core.mail import send_mail
from hackathon.models import Team, Edition
import os


@shared_task
def send_team_approval_email_to_students(team_id):
    team = Team.objects.get(id=team_id)
    edition = Edition.objects.get(id=team.edition.id)
    student_emails = list(team.students.all().values_list("email", flat=True))
    subject = f"Sua inscrição foi aceita para o Hackathon-IFC {edition.year}!"
    message = f"A inscrição do seu time para o Hackathon-IFC {edition.year} foi aceita!"

    send_mail(
        subject,
        message,
        os.getenv("EMAIL_HOST_USER"),  # from
        student_emails,  # to
        fail_silently=False,
    )
