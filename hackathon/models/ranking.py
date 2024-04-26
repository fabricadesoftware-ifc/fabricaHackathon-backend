from django.db import models

from .equipe import Equipe
from .edicao import Edicao

class Ranking(models.Model):
    equipe = models.ForeignKey(Equipe, on_delete=models.RESTRICT)
    nota_final = models.DecimalField(max_digits=3, decimal_places=1)
    classificacao = models.IntegerField()
    edicao = models.ForeignKey(Edicao, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.equipe.nome} - {self.notaFinal} - {self.classificacao}'
    
    class Meta:
        verbose_name = 'Ranking'
        verbose_name_plural = 'Rankings'
        ordering = ['edicao__ano', 'edicao__semestre', 'equipe__nome', 'classificacao']