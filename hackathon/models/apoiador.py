from django.db import models

from .edicao import Edicao

class Apoiador(models.Model):
    empresa = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='apoiadores', null=True, blank=True)
    link = models.URLField()
    edicao = models.ForeignKey(Edicao, on_delete=models.RESTRICT, null=True, blank=True)

    def __str__(self):
        return f'{self.empresa}'
    
    class Meta:
        verbose_name = 'Apoiador'
        verbose_name_plural = 'Apoiadores'
        ordering = ['empresa']