from celery import shared_task
from django.core.mail import send_mail
from hackathon.models import Team, Student
import os


@shared_task
def send_team_rejection_email_to_students(team_id):
    team = Team.objects.get(id=team_id)
    edition = Team.edition
    student_emails = list(team.students.all().values_list("email", flat=True))
    subject = f"Sua inscrição foi recusada para o Hackathon-IFC {edition.year}!"
    message = f"A inscrição do seu time para o Hackathon-IFC {edition.year} foi recusada. Por favor refaça a inscrição pelo website."

    send_mail(
        subject,
        message,
        os.getenv("EMAIL_HOST_USER"),  # from
        student_emails,  # to
        fail_silently=False,
    )
