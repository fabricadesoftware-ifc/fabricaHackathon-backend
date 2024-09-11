from hackathon.models import Supporter, Edition
from hackathon.resources.data_supporter import supporters

def populate_supporters():
    if Supporter.objects.exists():
        return

    supporters_to_insert = [Supporter(**supporter) for supporter in supporters]
    editions = list(Edition.objects.all())

    for index, supporter in enumerate(supporters_to_insert):
        if index < len(editions):
            supporter.edition = editions[index]
        else:
            supporter.edition = editions[index % len(editions)]

    Supporter.objects.bulk_create(supporters_to_insert)