from celery import shared_task
from django.core.mail import send_mail
from hackathon.models import Student, Edition

@shared_task
def send_emails_to_students(edition_id):
    edition = Edition.objects.get(id=edition_id)
    courses = edition.courses.all()
    student_emails = list(
        Student.objects.filter(classInfo__id__in=edition.involved_classes.all()).values_list('email', flat=True)
    )
    subject = f"Inscrições abertas para o Hackathon {edition.year} ({getCourses(courses, ', ')})"
    message = f"As inscrições para o Hackathon {edition.year} estão abertas, inscreva sua equipe! \n Cursos: \n {getCourses(courses, '\n')}"

    print(student_emails)

    send_mail(
        subject,
        message,
        'fabrica.hackathon@gmail.com', #from
        student_emails, #to
        fail_silently=False,
    )

def getCourses(edition_courses, join_string):
    resulting_string = join_string.join(course.name for course in edition_courses)
    return resulting_string