from django.db import models
from .edition import Edition

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    edition = models.ForeignKey(Edition, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']