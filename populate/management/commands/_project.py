from hackathon.models import Project, Category
from populate.resources.data_project import generate_projects
from populate.resources.data_team import teams

def populate_projects():
    if Project.objects.exists():
        return

    categories = list(Category.objects.all())

    projects = [Project(**project) for project in generate_projects(len(teams))]

    for index, project in enumerate(projects):
        project.category = categories[index % len(categories)]

    Project.objects.bulk_create(projects)
