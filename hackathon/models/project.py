from django.db import models
from .team import Team
from uploader.models import Image


class Project(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    deploy_link = models.URLField(null=True, blank=True)
    repository_link = models.URLField(null=True, blank=True)
    presentation_link = models.URLField(null=True, blank=True)
    video_link = models.URLField(null=True, blank=True)
    pitch_link = models.URLField(null=True, blank=True)
    category = models.ForeignKey(
        "Category", on_delete=models.RESTRICT, null=True, blank=True
    )
    photo = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )
    team_id = models.OneToOneField(
        Team, on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(null=True, blank=True)
