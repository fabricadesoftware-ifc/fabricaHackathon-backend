from django.db import models

from .student import Student
from .edition import Edition

class Team(models.Model):
    STATUS_CHOICES = [
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('pending', 'Pending')
    ]
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
    photo_team = models.ImageField(upload_to='teams', null=True, blank=True)
    leader = models.ForeignKey(Student, on_delete=models.RESTRICT, related_name='leader', null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending') 

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
        ordering = ['name']
