from django.db import models

from .avaliator import Avaliator
from .course import Course
from .criterion import Criterion
from .class_info import ClassInfo

class Edition(models.Model):
    year = models.IntegerField()
    semester = models.IntegerField()
    courses = models.ManyToManyField(Course)
    involved_classes = models.ManyToManyField(ClassInfo)
    edition_photo = models.ImageField(upload_to='editions', null=True, blank=True)
    applications_accepted = models.BooleanField(default=True, null=True, blank=True)
    registration_deadline = models.DateField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    finish_date = models.DateField(null=True, blank=True)
    min_members = models.IntegerField(null=True, blank=True)
    max_members = models.IntegerField(null=True, blank=True)
    avaliator = models.ManyToManyField(Avaliator)
    criterion = models.ManyToManyField(Criterion)

    def __str__(self):
        return f'{self.year}.{self.semester}'

    class Meta:
        verbose_name = 'Edition'
        verbose_name_plural = 'Editions'
        ordering = ['year', 'semester']