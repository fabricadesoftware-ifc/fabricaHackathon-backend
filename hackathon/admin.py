from django.contrib import admin

from .models import Curso, Turma, Edicao, Aluno, Equipe, Avaliador, Criterio, EdicaoCriterio, Avaliacao, AvaliadorEdicao

admin.site.register(Curso)
admin.site.register(Turma)
admin.site.register(Edicao)
admin.site.register(Aluno)
admin.site.register(Equipe)
admin.site.register(Avaliador)
admin.site.register(Criterio)
admin.site.register(EdicaoCriterio)
admin.site.register(Avaliacao)
admin.site.register(AvaliadorEdicao)
