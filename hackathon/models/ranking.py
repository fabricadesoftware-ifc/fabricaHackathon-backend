from django.db import models

from .team import Team
from .edition import Edition

class Ranking(models.Model):
    team = models.ForeignKey(Team, on_delete=models.RESTRICT)
    final_grade = models.DecimalField(max_digits=3, decimal_places=1)
    classification = models.IntegerField()
    edition = models.ForeignKey(Edition, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.team.name} - {self.final_grade} - {self.classification}'
    
    class Meta:
        verbose_name = 'Ranking'
        verbose_name_plural = 'Rankings'
        ordering = ['classification']