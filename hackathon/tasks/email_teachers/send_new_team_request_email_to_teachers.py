from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User, Group
from hackathon.models import Student, Team, Edition

@shared_task
def send_new_team_request_email_to_teachers(team_id):
    team = Team.objects.get(id=team_id)
    edition = team.edition
    students = team.students.all()
    leader = team.leader

    teachers_group = Group.objects.get(name='Teachers')
    teacher_emails = list(teachers_group.user_set.values_list('email', flat=True))

    subject = f"New Team Request for {edition.year} Edition"
    message = f"Dear Teachers,\n\nA new team request has been made for the {edition.year} Edition.\n"
    message += f"Team Leader: {leader.name} ({leader.email})\n\nTeam Members:\n"
    message += "\n".join([f"{student.name} ({student.email})" for student in students])

    send_mail(
        subject,
        message,
        'fabrica.hackathon@gmail.com',  # from
        teacher_emails,  # to
        fail_silently=False,
    )
