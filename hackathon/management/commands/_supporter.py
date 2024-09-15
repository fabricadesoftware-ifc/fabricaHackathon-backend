from hackathon.models import Supporter, Edition
from hackathon.resources.data_supporter import supporters

def populate_supporters():
    if Supporter.objects.exists():
        return

    supporters_to_insert = [Supporter(**supporter) for supporter in supporters]

    Supporter.objects.bulk_create(supporters_to_insert)