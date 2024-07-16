from django.db import models

from .classe import Classe

class Student(models.Model):
    name = models.CharField(max_length=100)
    registration = models.CharField(max_length=10)
    classe = models.ForeignKey(Classe, on_delete=models.RESTRICT)
    whatsapp = models.CharField(max_length=15)
    email = models.EmailField()
    github = models.URLField()
    portfolio = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ['name']