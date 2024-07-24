from django.db import models

from .team import Team
from .avaliator import Avaliator
from .criterion import Criterion

class Avaliation(models.Model):
    avaliator = models.ForeignKey(Avaliator, on_delete=models.RESTRICT)
    team = models.ForeignKey(Team, on_delete=models.RESTRICT)
    criterion = models.ForeignKey(Criterion, on_delete=models.RESTRICT)
    note = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return f'{self.avaliator.name} - {self.team.name} - {self.criterion.description} - {self.note}'

    class Meta:
        verbose_name = 'Avaliation'
        verbose_name_plural = 'Avaliations'