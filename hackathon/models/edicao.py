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

    def __str__(self):
        return f'{self.ano}.{self.semestre}'
    
    class Meta:
        verbose_name = 'Edição'
        verbose_name_plural = 'Edições'
        ordering = ['ano', 'semestre']


class AvaliadorEdicao(models.Model):
    avaliador = models.ForeignKey(Avaliador, on_delete=models.RESTRICT)
    edicao = models.ForeignKey(Edicao, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.avaliador} - {self.edicao.ano}.{self.edicao.semestre}'
    
    class Meta:
        verbose_name = 'Avaliador da Edição'
        verbose_name_plural = 'Avaliadores das Edições'
        ordering = ['avaliador', 'edicao__ano', 'edicao__semestre']

class EdicaoCriterio(models.Model):
    edicao = models.ForeignKey(Edicao, on_delete=models.RESTRICT)
    criterio = models.ForeignKey(Criterio, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.edicao.ano}.{self.edicao.semestre} - {self.criterio}'
    
    class Meta:
        verbose_name = 'Critério da Edição'
        verbose_name_plural = 'Critérios das Edições'
        ordering = ['edicao__ano', 'edicao__semestre', 'criterio']