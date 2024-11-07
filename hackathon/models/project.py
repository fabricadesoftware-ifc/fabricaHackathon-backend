from django.db import models
from .images import Images

class Project(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    deploy_link = models.URLField(null=True, blank=True)
    repository_link = models.URLField(null=True, blank=True)
    presentation_link = models.URLField(null=True, blank=True)
    video_link = models.URLField(null=True, blank=True)
    pitch_link = models.URLField(null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.RESTRICT, null=True, blank=True)
    project_photo_base64 = models.OneToOneField(Images, on_delete=models.CASCADE, null=True, blank=True)
