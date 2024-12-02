from django.db.models import Q
from hackathon.models import Team, Edition
from user.models import StudentProfile
from populate.resources.data_team import teams
from io import BytesIO
from PIL import Image as PILImage
import mimetypes
from django.core.files.base import ContentFile
import requests
from uploader.models import Image as UploadedImage

from faker import Faker

fake = Faker("pt_BR")


def populate_teams():
    if Team.objects.exists():
        return

    teams_to_insert = []

    for index, team_data in enumerate(teams):
        response = requests.get("https://picsum.photos/800")

        if response.status_code == 200:
            image_data = BytesIO(response.content)
            pil_image = PILImage.open(image_data)

            image_buffer = BytesIO()
            pil_image.save(image_buffer, format="JPEG")
            image_buffer.seek(0)

            content_type, _ = mimetypes.guess_type("sample_image.jpg")
            if content_type is None:
                content_type = "image/jpeg"

            image_file = ContentFile(image_buffer.read(), name="sample_image.jpg")

            image = UploadedImage(
                file=image_file,
                description="Sample image for edition",
                content_type=content_type,
            )
            image.save()
        else:
            image = None

        team = Team(
            name=team_data["name"],
            registration_date=team_data["registration_date"],
            valid_registration=team_data["valid_registration"],
            photo=image,
        )

        if index % 2 == 0:
            editions = list(Edition.objects.filter(courses__acronym__in=["MCC", "DCC"]))
            if index < len(editions):
                team.edition = editions[index]
            else:
                team.edition = editions[index % len(editions)]

            team.leader = StudentProfile.objects.filter(
                class_info__course__acronym__in=["MCC", "DCC"]
            ).first()

        else:
            editions = list(
                Edition.objects.filter(courses__acronym__in=["INFO", "BSI"])
            )
            if index <= len(editions):
                team.edition = editions[index]
            else:
                team.edition = editions[index % len(editions)]

            team.leader = StudentProfile.objects.filter(
                class_info__course__acronym__in=["INFO", "BSI"]
            ).first()

        edition_categories = list(team.edition.categories.all())
        if index < len(edition_categories):
            team.category = edition_categories[index]
        else:
            team.category = edition_categories[index % len(edition_categories)]

        teams_to_insert.append(team)

    Team.objects.bulk_create(teams_to_insert)

    created_teams = list(Team.objects.all())
    student_group_one = StudentProfile.objects.filter(
        Q(class_info__course__acronym__in=["MCC", "DCC"])
    )
    student_group_two = StudentProfile.objects.filter(
        Q(class_info__course__acronym__in=["INFO", "BSI"])
    )

    for index, team in enumerate(created_teams):
        team.save()
        if index % 2 == 0:
            team.students.set(student_group_one)
        else:
            team.students.set(student_group_two)
