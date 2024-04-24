from django.db import models

from .aluno import Aluno
from .edicao import Edicao

class Equipe(models.Model):
    nome = models.CharField(max_length=100)
    alunos = models.ManyToManyField(Aluno)
    edicao = models.ForeignKey(Edicao, on_delete=models.RESTRICT)
    linkDeploy = models.URLField(null=True, blank=True)
    linkRepositorio = models.URLField(null=True, blank=True)
    linkApresentacao = models.URLField(null=True, blank=True)
    linkVideo = models.URLField(null=True, blank=True)
    linkPitch = models.URLField(null=True, blank=True)
    dataInscricao = models.DateField(auto_now_add=True, null=True, blank=True)
    inscricaoValidada = models.BooleanField(default=False, null=True, blank=True)
    fotoEquipe = models.ImageField(upload_to='equipes', null=True, blank=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'
        ordering = ['nome']