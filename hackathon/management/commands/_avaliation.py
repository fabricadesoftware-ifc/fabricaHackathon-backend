from hackathon.models import Criterion
from hackathon.resources.data_avaliation import criteria

def populate_criteria():
    if Criterion.objects.exists():
        return

    criteria_to_insert = [Criterion(**criterion) for criterion in criteria]
    Criterion.objects.bulk_create(criteria_to_insert)