from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    sigla = models.CharField(max_length=10)
    nivel_curso = models.CharField(
        max_length=10,
        choices=[
            ('tecn', 'Técnico'),
            ('grad', 'Graduação'),
            ('posgrad', 'Pós-Graduação'),
            ('mest', 'Mestrado'),
            ('dout', 'Doutorado')
        ]
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['nome']