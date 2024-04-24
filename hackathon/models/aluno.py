from django.db import models

from .turma import Turma

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=10)
    turma = models.ForeignKey(Turma, on_delete=models.RESTRICT)
    whatsapp = models.CharField(max_length=15)
    email = models.EmailField()
    github = models.URLField()
    portfolio = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['nome']