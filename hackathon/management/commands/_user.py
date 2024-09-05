from django.contrib.auth.models import User
from hackathon.models import Student, Avaliator, ClassInfo

from hackathon.resources.data_user import students


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

    students_to_insert = [Student(**student) for student in students]
    class_infos = list(ClassInfo.objects.all())
    students_per_class = max(1, len(students_to_insert) // len(class_infos))

    for index, student in enumerate(students_to_insert):
        class_index = index // students_per_class

        class_info = class_infos[class_index % len(class_infos)]
        student.class_info = class_info
    
    Student.objects.bulk_create(students_to_insert)