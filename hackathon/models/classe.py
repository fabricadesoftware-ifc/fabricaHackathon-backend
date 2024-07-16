from django.db import models

from .course import Course

class Classe(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Classe'
        verbose_name_plural = 'Classes'
        ordering = ['name']