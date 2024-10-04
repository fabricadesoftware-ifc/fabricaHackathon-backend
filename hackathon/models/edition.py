from django.db import models
from .course import Course
from .criterion import Criterion
from .class_info import ClassInfo
from .category import Category
from .supporter import Supporter
from .images import Images
from user.models import CustomUser

class Edition(models.Model):
    year = models.IntegerField()
    semester = models.IntegerField()
    courses = models.ManyToManyField(Course)
    involved_classes = models.ManyToManyField(ClassInfo)
    photo_base64_edition = models.OneToOneField(Images, on_delete=models.CASCADE, null=True, blank=True)
    applications_accepted = models.BooleanField(default=True, null=True, blank=True)
    registration_deadline = models.DateField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    finish_date = models.DateField(null=True, blank=True)
    min_members = models.IntegerField(null=True, blank=True)
    max_members = models.IntegerField(null=True, blank=True)
    avaliators = models.ManyToManyField(CustomUser, limit_choices_to={"is_avaliator": True})
    criteria = models.ManyToManyField(Criterion)
    categories = models.ManyToManyField(Category)
    supporters = models.ManyToManyField(Supporter)

    def __str__(self):
        return f"{self.year}.{self.semester}"

    class Meta:
        verbose_name = "Edition"
        verbose_name_plural = "Editions"
        ordering = ["year", "semester"]
