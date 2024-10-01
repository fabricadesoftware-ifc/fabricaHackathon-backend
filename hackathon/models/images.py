from django.db import models

class Images(models.Model):
    photo_base64 = models.TextField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.description or 'No description'

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
        ordering = ["photo_base64"]
