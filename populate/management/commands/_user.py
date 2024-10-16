from django.contrib.auth.models import Group
from hackathon.models import ClassInfo
from user.models import CustomUser, StudentProfile
from populate.resources.data_user import students, avaliators, teachers


def __get_or_create_super_user() -> None:
    try:
        CustomUser.objects.get(name="admin")
    except CustomUser.DoesNotExist:
        CustomUser.objects.create_superuser(
            email="admin@admin.com", name="admin", password="admin"
        )


def populate_users():
    if CustomUser.objects.exists():
        return

    __get_or_create_super_user()


def populate_students():
    if CustomUser.objects.filter(groups__name="Students").exists():
        return

    students_group, created = Group.objects.get_or_create(name="Students")
    class_infos = list(ClassInfo.objects.all())

    students_to_insert = [
        CustomUser(name=student["name"], email=student["email"]) for student in students
    ]
    students_per_class = max(1, len(students_to_insert) // len(class_infos))

    for index, student in enumerate(students):
        class_index = index // students_per_class

        class_info = class_infos[class_index % len(class_infos)]
        student["student_profile"]["class_info"] = class_info

    CustomUser.objects.bulk_create(students_to_insert)

    for student in CustomUser.objects.filter(
        email__in=[std["email"] for std in students]
    ):
        student.groups.add(students_group)
        student.set_password(
            next(s["password"] for s in students if s["email"] == student.email)
        )
        student.save()

        student_profile_data = next(
            s["student_profile"] for s in students if s["email"] == student.email
        )

        StudentProfile.objects.update_or_create(
            user=student, defaults=student_profile_data
        )


def populate_avaliators():
    if CustomUser.objects.filter(groups__name="Avaliators").exists():
        return

    avaliators_group, created = Group.objects.get_or_create(name="Avaliators")

    avaliators_to_insert = [
        CustomUser(name=avaliator["name"], email=avaliator["email"], is_avaliator=True)
        for avaliator in avaliators
    ]
    CustomUser.objects.bulk_create(avaliators_to_insert)

    for avaliator in CustomUser.objects.filter(
        email__in=[avl["email"] for avl in avaliators]
    ):
        avaliator.groups.add(avaliators_group)
        avaliator.set_password(
            next(a["password"] for a in avaliators if a["email"] == avaliator.email)
        )
        avaliator.save()


def populate_teachers():
    if CustomUser.objects.filter(groups__name="Teachers").exists():
        return

    teachers_group, created = Group.objects.get_or_create(name="Teachers")

    teachers_to_insert = [
        CustomUser(name=teacher["name"], email=teacher["email"]) for teacher in teachers
    ]
    CustomUser.objects.bulk_create(teachers_to_insert)

    for teacher in CustomUser.objects.filter(
        email__in=[tch["email"] for tch in teachers]
    ):
        teacher.groups.add(teachers_group)
        teacher.set_password(
            next(t["password"] for t in teachers if t["email"] == teacher.email)
        )
        teacher.save()
