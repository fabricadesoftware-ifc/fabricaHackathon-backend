from hackathon.models import Team, Student, Edition, Category
from hackathon.resources.data_team import teams, categories

def populate_teams():
    if Team.objects.exists():
        return

    teams_to_insert = [Team(**team) for team in teams]

    for index, team in enumerate(teams_to_insert):
        if index % 2 == 0:
            editions = list(Edition.objects.filter(courses__acronym__in=["MCC", "DCC"]))
            if index < len(editions):
                team.edition = editions[index]
            else:
                team.edition = editions[index % len(editions)]

            team.leader = Student.objects.filter(
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

            team.leader = Student.objects.filter(
                class_info__course__acronym__in=["INFO", "BSI"]
            ).first()
        
        edition_categories = Category.objects.filter(edition=team.edition)

        if index < len(edition_categories):
            team.category = edition_categories[index]
        else:
            team.category = edition_categories[index % len(edition_categories)]

    Team.objects.bulk_create(teams_to_insert)

    created_teams = list(Team.objects.all())

    for index, team in enumerate(created_teams):
        if index % 2 == 0:
            team.students.set(
                Student.objects.filter(class_info__course__acronym__in=["MCC", "DCC"])
            )
        else:
            team.students.set(
                Student.objects.filter(class_info__course__acronym__in=["INFO", "BSI"])
            )
        
def populate_categories():
    if Category.objects.exists():
        return

    categories_to_insert = [Category(**category) for category in categories]
    editions = list(Edition.objects.all())
    
    for index, category in enumerate(categories_to_insert):
        if index < len(editions):
            category.edition = editions[index]
        else:
            category.edition = editions[index % len(editions)]
        
    Category.objects.bulk_create(categories_to_insert)