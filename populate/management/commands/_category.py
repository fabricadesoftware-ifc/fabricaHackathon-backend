from hackathon.models import Category
from populate.resources.data_team import categories

def populate_categories():
    if Category.objects.exists():
        return

    categories_to_insert = [Category(**category) for category in categories]
        
    Category.objects.bulk_create(categories_to_insert)