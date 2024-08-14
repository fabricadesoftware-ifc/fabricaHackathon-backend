from celery import shared_task
from django.core.mail import send_mail
from hackathon.models import Student, Edition

@shared_task
def send_emails_to_students(edition_id):
    edition = Edition.objects.get(id=edition_id)
    student_emails = list(Student.objects.values_list('email', flat=True))
    courses = getCourses(edition.courses.all())
    subject = f"Inscrições abertas para o Hackathon {edition.year} ({courses})"
    message = f"As inscrições para o Hackathon {edition.year} estão abertas, inscreva sua equipe! \n Cursos: \n {courses}"

    send_mail(
        subject,
        message,
        'fabrica.hackathon@gmail.com', #from
        student_emails, #to
        fail_silently=False,
    )

def getCourses(edition_courses):
    resulting_string = "\n".join(course.name for course in edition_courses)
    return resulting_string