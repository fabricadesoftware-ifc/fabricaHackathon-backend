import base64
import requests
from hackathon.models import (
    Course,
    Edition,
    Avaliator,
    Criterion,
    ClassInfo,
    Category,
    Supporter,
)
from hackathon.resources.data_edition import editions


def fetch_random_image_base64():
    url = "https://random.imagecdn.app/v1/image?width=1280&height=720&category=dogs&format=json"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        image_url = data.get("url")

        if image_url:
            image_response = requests.get(image_url)

            if image_response.status_code == 200:
                return base64.b64encode(image_response.content).decode("utf-8")

    return None


def populate_editions():
    if Edition.objects.exists():
        return

    editions_to_insert = []
    for edition in editions:
        edition_photo_base64 = fetch_random_image_base64()
        edition["edition_photo_base64"] = edition_photo_base64
        editions_to_insert.append(Edition(**edition))

    avaliators = list(Avaliator.objects.all())
    criteria = list(Criterion.objects.all())
    all_categories = list(Category.objects.all())
    supporters = list(Supporter.objects.all())

    Edition.objects.bulk_create(editions_to_insert)

    created_editions = list(Edition.objects.all())

    for index, edition in enumerate(created_editions):
        if index % 2 == 0:
            courses = list(Course.objects.filter(acronym__in=["MCC", "DCC"]))
            classes = list(ClassInfo.objects.filter(course__acronym__in=["MCC", "DCC"]))
            categories = list(Category.objects.filter(id__lt=len(all_categories) // 2))
        else:
            courses = list(Course.objects.filter(acronym__in=["INFO", "BSI"]))
            classes = list(
                ClassInfo.objects.filter(course__acronym__in=(["INFO", "BSI"]))
            )
            categories = list(Category.objects.filter(id__gte=len(all_categories) // 2))

        edition.courses.set(courses)
        edition.avaliators.set(avaliators)
        edition.criteria.set(criteria)
        edition.involved_classes.set(classes)
        edition.categories.set(categories)
        edition.supporters.set(supporters)
