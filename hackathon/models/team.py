from django.db import models

from user.models import StudentProfile as Student
from .edition import Edition
from uploader.models import Image


class Team(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name="students")
    edition = models.ForeignKey(Edition, on_delete=models.RESTRICT)
    leader = models.ForeignKey(
        Student, on_delete=models.RESTRICT, related_name="leader"
    )
    verification_token = models.CharField(max_length=100, blank=True, null=True)
    valid_registration = models.BooleanField(default=False, null=True, blank=True)
    registration_date = models.DateField(auto_now_add=True, null=True, blank=True)
    photo = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"
        ordering = ["name"]
