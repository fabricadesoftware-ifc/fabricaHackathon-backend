from django.db import models

from .team import Team
from user.models import CustomUser
from .criterion import Criterion


class Avaliation(models.Model):
    avaliator = models.ForeignKey(
        CustomUser,
        on_delete=models.RESTRICT,
        limit_choices_to={"is_avaliator": True},
    )
    team = models.ForeignKey(Team, on_delete=models.RESTRICT)
    criterion = models.ForeignKey(Criterion, on_delete=models.RESTRICT)
    grade = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.avaliator.name} - {self.team.name} - {self.criterion.description} - {self.grade}"

    class Meta:
        verbose_name = "Avaliation"
        verbose_name_plural = "Avaliations"
