from django.contrib.auth.models import Group
from hackathon.models import Student, ClassInfo
from user.models import CustomUser
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

def populate_avaliators():
    # Check if any Avaliators exist
    if CustomUser.objects.filter(groups__name="Avaliators").exists():
        return

    # Get or create the Avaliators group
    avaliators_group, created = Group.objects.get_or_create(name="Avaliators")

    # Create Avaliators users
    avaliators_to_insert = [
        CustomUser(name=avaliator["name"], email=avaliator["email"], is_avaliator=True)
        for avaliator in avaliators
    ]
    CustomUser.objects.bulk_create(avaliators_to_insert)

    # Add created users to the Avaliators group
    for avaliator in CustomUser.objects.filter(email__in=[avl["email"] for avl in avaliators]):
        avaliator.groups.add(avaliators_group)
        avaliator.set_password(next(a["password"] for a in avaliators if a["email"] == avaliator.email))
        avaliator.save()

def populate_teachers():
    # Check if any Teachers exist
    if CustomUser.objects.filter(groups__name="Teachers").exists():
        return

    # Get or create the Teachers group
    teachers_group, created = Group.objects.get_or_create(name="Teachers")

    # Create Teachers users
    teachers_to_insert = [
        CustomUser(name=teacher["name"], email=teacher["email"])
        for teacher in teachers
    ]
    CustomUser.objects.bulk_create(teachers_to_insert)

    # Add created users to the Teachers group
    for teacher in CustomUser.objects.filter(email__in=[tch["email"] for tch in teachers]):
        teacher.groups.add(teachers_group)
        teacher.set_password(next(t["password"] for t in teachers if t["email"] == teacher.email))
        teacher.save()