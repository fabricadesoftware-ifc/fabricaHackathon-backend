from django.db import models

class Criterio(models.Model):
    descricao = models.TextField()
    peso = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name = 'Critério'
        verbose_name_plural = 'Critérios'
        ordering = ['descricao']