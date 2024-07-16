from django.db import models

from .edition import Edition

class Supporter(models.Model):
    company = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='supporters', null=True, blank=True)
    link = models.URLField()
    edition = models.ForeignKey(Edition, on_delete=models.RESTRICT, null=True, blank=True)

    def __str__(self):
        return f'{self.company}'
    
    class Meta:
        verbose_name = 'Supporter'
        verbose_name_plural = 'Supporters'
        ordering = ['company']