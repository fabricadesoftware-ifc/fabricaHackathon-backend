from django.contrib import admin

from .models import curso, turma, edicao, aluno, equipe, avaliador, criterio, edicao_criterio, avaliacao, avaliador_edicao

admin.site.register(curso)
admin.site.register(turma)
admin.site.register(edicao)
admin.site.register(aluno)
admin.site.register(equipe)
admin.site.register(avaliador)
admin.site.register(criterio)
admin.site.register(edicao_criterio)
admin.site.register(avaliacao)
admin.site.register(avaliador_edicao)
