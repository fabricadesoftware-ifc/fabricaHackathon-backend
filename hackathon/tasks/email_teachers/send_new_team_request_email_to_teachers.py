from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import Group
from hackathon.models import Team


@shared_task
def send_new_team_request_email_to_teachers(
    team_id, accept_team_link, reject_team_link
):
    team = Team.objects.get(id=team_id)
    print(team)
    edition = team.edition
    students = team.students.all()
    leader = team.leader

    teachers_group = Group.objects.get(name="Teachers")
    teacher_emails = list(teachers_group.user_set.values_list("email", flat=True))

    subject = f"""Novo pedido de inscrição para o Hackathon {edition.year}"""
    message = f"""Há um novo pedido de inscrição de equipe para o Hackathon {edition.year}
                
                Equipe: {team.name}
                Lider: {leader}
                Alunos:
                {("/n").join(get_student_names_and_classes(students))}

                Clique no link abaixo para aceitar a submissão:
                {accept_team_link}
                Clique no link abaixo para rejeitar a submissão:
                {reject_team_link}
    """

    send_mail(
        subject,
        message,
        "fabrica.hackathon@gmail.com",  # from
        teacher_emails,  # to
        fail_silently=False,
    )


def get_student_names_and_classes(students):
    students_and_classes = []
    for student in students:
        students_and_classes.append(f"{student.user.name} ({student.class_info.name})")

    return students_and_classes
