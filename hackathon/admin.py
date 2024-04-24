from django.contrib import admin

from .models import Curso, Turma, Edicao, Aluno, Equipe, Avaliador, Criterio, Edicao_criterio, Avaliacao, Avaliador_edicao

admin.site.register(Curso)
admin.site.register(Turma)
admin.site.register(Edicao)
admin.site.register(Aluno)
admin.site.register(Equipe)
admin.site.register(Avaliador)
admin.site.register(Criterio)
admin.site.register(Edicao_criterio)
admin.site.register(Avaliacao)
admin.site.register(Avaliador_edicao)
