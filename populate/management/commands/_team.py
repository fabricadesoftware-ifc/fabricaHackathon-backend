import base64
import requests
from hackathon.models import Team, Edition, Images
from user.models import StudentProfile
from populate.resources.data_team import teams


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


def populate_teams():
    if Team.objects.exists():
        return

    teams_to_insert = []
    
    for index, team_data in enumerate(teams):
        team_photo_base64 = fetch_random_image_base64()
        images_to_insert = []

        if team_photo_base64:
            image_instance = Images(photo_base64=team_photo_base64)
            images_to_insert.append(image_instance)
        else:
            image_instance = None

        team = Team(
            name=team_data["name"],
            deploy_link=team_data["deploy_link"],
            repository_link=team_data["repository_link"],
            presentation_link=team_data["presentation_link"],
            video_link=team_data["video_link"],
            pitch_link=team_data["pitch_link"],
            registration_date=team_data["registration_date"],
            valid_registration=team_data["valid_registration"],
            photo_base64_team=image_instance,
        )

        Images.objects.bulk_create(images_to_insert)
        
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
    student_group_one = StudentProfile.objects.filter(class_info__course__acronym__in=["MCC", "DCC"])
    student_group_two = StudentProfile.objects.filter(class_info__course__acronym__in=["INFO", "BSI"])

    for index, team in enumerate(created_teams):
        if index % 2 == 0:
            team.students.set(student_group_one)
        else:
            team.students.set(student_group_two)
