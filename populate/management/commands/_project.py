import base64
import requests
from hackathon.models import Project, Images, Category, Team
from populate.resources.data_project import generate_projects
from populate.resources.data_team import teams

def populate_projects():
    if Project.objects.exists():
        return

    categories = list(Category.objects.all())
    team_instances = list(Team.objects.all())
    projects = generate_projects(len(teams))

    project_instances = []

    for index, project_data in enumerate(projects):
        response = requests.get("https://picsum.photos/800")
        image_base64 = base64.b64encode(response.content).decode("utf-8")
        project_image = Images.objects.create(photo_base64=image_base64, description=f"Image for project {index + 1}")

        project_instance = Project(
            name=project_data["name"],
            deploy_link=project_data["deploy_link"],
            repository_link=project_data["repository_link"],
            presentation_link=project_data["presentation_link"],
            video_link=project_data["video_link"],
            pitch_link=project_data["pitch_link"],
            category=categories[index % len(categories)],
            team_id=team_instances[index % len(team_instances)],
            project_photo_base64=project_image,  
        )
        project_instances.append(project_instance)

    Project.objects.bulk_create(project_instances)

