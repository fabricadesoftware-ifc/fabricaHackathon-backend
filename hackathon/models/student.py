from django.db import models

from .classInfo import ClassInfo

class Student(models.Model):
    name = models.CharField(max_length=100)
    registration = models.CharField(max_length=10)
    classInfo = models.ForeignKey(ClassInfo, on_delete=models.RESTRICT, verbose_name='class')
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