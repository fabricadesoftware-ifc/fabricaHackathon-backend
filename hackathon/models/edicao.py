from django.db import models

from .avaliador import Avaliador
from .curso import Curso
from .criterio import Criterio
from .turma import Turma

class Edicao(models.Model):
    ano = models.IntegerField()
    semestre = models.IntegerField()
    cursos = models.ManyToManyField(Curso)
    turmas_envolvidas = models.ManyToManyField(Turma)
    foto_edicao = models.ImageField(upload_to='edicoes', null=True, blank=True)
    aceita_inscricoes = models.BooleanField(default=True, null=True, blank=True)
    prazo_inscricoes = models.DateField(null=True, blank=True)
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    quantidade_membros_equipe = models.IntegerField(null=True, blank=True)
    avaliador = models.ManyToManyField(Avaliador)
    criterio = models.ManyToManyField(Criterio)

    def __str__(self):
        return f'{self.ano}.{self.semestre}'
    
    class Meta:
        verbose_name = 'Edição'
        verbose_name_plural = 'Edições'
        ordering = ['ano', 'semestre']