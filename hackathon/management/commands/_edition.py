from hackathon.models import Course, Edition, Avaliator, Criterion
from hackathon.resources.data_edition import editions
from hackathon.resources.data_avaliation import criteria

def populate_editions():
    if Edition.objects.exists():
        return
    
    editions_to_insert = [Edition(**edition) for edition in editions]
    avaliators = list(Avaliator.objects.all())
    criteria = list(Criterion.objects.all())

    Edition.objects.bulk_create(editions_to_insert)

    created_editions = list(Edition.objects.all())

    for index, edition in enumerate(created_editions):
        if index % 2 == 0:
            courses = list(Course.objects.filter(acronym__in=["MCC", "DCC"]))
        else:
            courses = list(Course.objects.filter(acronym__in=["INFO", "BSI"]))
        
        edition.courses.set(courses)
        edition.avaliators.set(avaliators)
        edition.criteria.set(criteria)