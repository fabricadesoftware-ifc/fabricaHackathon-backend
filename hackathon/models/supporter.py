from django.db import models


class Supporter(models.Model):
    company = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='supporters', null=True, blank=True)
    link = models.URLField()

    def __str__(self):
        return f'{self.company}'
    
    class Meta:
        verbose_name = 'Supporter'
        verbose_name_plural = 'Supporters'
        ordering = ['company']