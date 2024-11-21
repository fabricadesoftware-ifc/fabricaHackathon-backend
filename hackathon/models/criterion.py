from django.db import models


class Criterion(models.Model):
    description = models.TextField()
    weight = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Criterion"
        verbose_name_plural = "Criteria"
        ordering = ["description"]
