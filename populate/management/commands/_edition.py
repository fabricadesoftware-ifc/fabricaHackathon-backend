import requests
from hackathon.models import (
    Course,
    Edition,
    Criterion,
    ClassInfo,
    Category,
    Supporter,
)
from django.core.files.base import ContentFile
from uploader.models import Image as UploadedImage
from user.models import CustomUser
from populate.resources.data_edition import editions
from io import BytesIO
from PIL import Image as PILImage
import mimetypes
from django.core.files.base import ContentFile


def populate_editions():
    if Edition.objects.exists():
        return

    editions_to_insert = []

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
    for edition in editions:
        new_edition = Edition(
            year=edition["year"],
            semester=edition["semester"],
            applications_accepted=edition["applications_accepted"],
            registration_deadline=edition["registration_deadline"],
            start_date=edition["start_date"],
            finish_date=edition["finish_date"],
            min_members=edition["min_members"],
            max_members=edition["max_members"],
            photo=image,
        )
        editions_to_insert.append(new_edition)

    for new_edition in editions_to_insert:
        new_edition.save()

    avaliators = list(CustomUser.objects.filter(groups__name="Avaliators"))
    criteria = list(Criterion.objects.all())
    all_categories = list(Category.objects.all())
    supporters = list(Supporter.objects.all())

    created_editions = list(Edition.objects.all())

    for index, edition in enumerate(created_editions):
        if index % 2 == 0:
            courses = list(Course.objects.filter(acronym__in=["MCC", "DCC"]))
            classes = list(ClassInfo.objects.filter(course__acronym__in=["MCC", "DCC"]))
            categories = list(Category.objects.filter(id__lt=len(all_categories) // 2))
        else:
            courses = list(Course.objects.filter(acronym__in=["INFO", "BSI"]))
            classes = list(
                ClassInfo.objects.filter(course__acronym__in=["INFO", "BSI"])
            )
            categories = list(Category.objects.filter(id__gte=len(all_categories) // 2))
        edition.courses.set(courses)
        edition.avaliators.set(avaliators)
        edition.criteria.set(criteria)
        edition.involved_classes.set(classes)
        edition.categories.set(categories)
        edition.supporters.set(supporters)
