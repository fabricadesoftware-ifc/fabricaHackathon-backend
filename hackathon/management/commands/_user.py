from django.contrib.auth.models import User
from hackathon.models import Student, Avaliator, Teacher, ClassInfo

from hackathon.resources.data_user import avaliators, students, teachers


def __get_or_create_super_user() -> None:
    try:
        User.objects.get(username="admin")
    except User.DoesNotExist:
        User.objects.create_superuser(
            email="admin@admin.com", username="admin", password="admin"
        )

def populate_users():
    if User.objects.exists():
        return

    __get_or_create_super_user()

def populate_students():
    if Student.objects.exists():
        return

    students_to_insert = [
        Student(**student)
        for student in students
    ]

    # for index, student in enumerate(students_to_insert):
    #     if index < 2:
    #         student.class_info = ClassInfo.objects.get(name="1info1")
    #     elif 