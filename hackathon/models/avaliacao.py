from django.db import models

from .equipe import Equipe
from .avaliador import Avaliador
from .criterio import Criterio

class Avaliacao(models.Model):
    avaliador = models.ForeignKey(Avaliador, on_delete=models.RESTRICT)
    equipe = models.ForeignKey(Equipe, on_delete=models.RESTRICT)
    criterio = models.ForeignKey(Criterio, on_delete=models.RESTRICT)
    nota = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return f'{self.avaliador.nome} - {self.equipe.nome} - {self.criterio.descricao} - {self.nota}'

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'