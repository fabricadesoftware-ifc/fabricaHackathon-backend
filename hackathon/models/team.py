from django.db import models

from user.models import StudentProfile as Student
from .edition import Edition
from .images import Images
# from .project import Project

class Team(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name='students')
    edition = models.ForeignKey(Edition, on_delete=models.RESTRICT)
    leader = models.ForeignKey(Student, on_delete=models.RESTRICT, related_name='leader')
    verification_token = models.CharField(max_length=100, blank=True, null=True)
    valid_registration = models.BooleanField(default=False, null=True, blank=True)
    registration_date = models.DateField(auto_now_add=True, null=True, blank=True)
    photo_base64_team= models.ForeignKey(Images, on_delete=models.CASCADE, null=True, blank=True)
    # project = models.ForeignKey(Project, on_delete=models.RESTRICT, null=True, blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
        ordering = ['name']
