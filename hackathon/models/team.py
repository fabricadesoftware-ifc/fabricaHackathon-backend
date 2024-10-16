from django.db import models

from user.models import StudentProfile as Student
from .edition import Edition
from .images import Images

class Team(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name='students')
    edition = models.ForeignKey(Edition, on_delete=models.RESTRICT)
    deploy_link = models.URLField(null=True, blank=True)
    repository_link = models.URLField(null=True, blank=True)
    presentation_link = models.URLField(null=True, blank=True)
    video_link = models.URLField(null=True, blank=True)
    pitch_link = models.URLField(null=True, blank=True)
    registration_date = models.DateField(auto_now_add=True, null=True, blank=True)
    valid_registration = models.BooleanField(default=False, null=True, blank=True)
    # photo_team = models.ImageField(upload_to='teams', null=True, blank=True)
    photo_base64_team= models.OneToOneField(Images, on_delete=models.CASCADE, null=True, blank=True)
    leader = models.ForeignKey(Student, on_delete=models.RESTRICT, related_name='leader')
    category = models.ForeignKey('Category', on_delete=models.RESTRICT, null=True, blank=True)
    verification_token = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
        ordering = ['name']
