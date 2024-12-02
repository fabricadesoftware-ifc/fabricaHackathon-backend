import requests
from hackathon.models import Project, Category, Team
from populate.resources.data_project import generate_projects
from populate.resources.data_team import teams
from uploader.models import Image as UploadedImage
from io import BytesIO
from PIL import Image as PILImage
import mimetypes
from django.core.files.base import ContentFile


def populate_projects():
    if Project.objects.exists():
        return

    categories = list(Category.objects.all())
    team_instances = list(Team.objects.all())
    projects = generate_projects(len(teams))

    project_instances = []

    for index, project_data in enumerate(projects):
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

        project_instance = Project(
            name=project_data["name"],
            deploy_link=project_data["deploy_link"],
            repository_link=project_data["repository_link"],
            presentation_link=project_data["presentation_link"],
            video_link=project_data["video_link"],
            pitch_link=project_data["pitch_link"],
            category=categories[index % len(categories)],
            team_id=team_instances[index % len(team_instances)],
            description=project_data["description"],
            photo=image,
        )
        project_instances.append(project_instance)

    Project.objects.bulk_create(project_instances)
