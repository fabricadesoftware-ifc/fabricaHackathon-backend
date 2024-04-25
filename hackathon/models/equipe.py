from django.db import models

from .aluno import Aluno
from .edicao import Edicao

class Equipe(models.Model):
    nome = models.CharField(max_length=100)
    alunos = models.ManyToManyField(Aluno)
    edicao = models.ForeignKey(Edicao, on_delete=models.RESTRICT)
    link_deploy = models.URLField(null=True, blank=True)
    link_repositorio = models.URLField(null=True, blank=True)
    link_apresentacao = models.URLField(null=True, blank=True)
    link_video = models.URLField(null=True, blank=True)
    link_pitch = models.URLField(null=True, blank=True)
    data_inscricao = models.DateField(auto_now_add=True, null=True, blank=True)
    inscricao_validada = models.BooleanField(default=False, null=True, blank=True)
    foto_equipe = models.ImageField(upload_to='equipes', null=True, blank=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'
        ordering = ['nome']