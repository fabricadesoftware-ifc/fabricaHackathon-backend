from django.db import models

class curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    sigla = models.CharField(max_length=10)
    nivelCurso = models.CharField(
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

class turma(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.ForeignKey(curso, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
        ordering = ['nome']

class edicao(models.Model):
    ano = models.IntegerField()
    semestre = models.IntegerField()
    cursos = models.ManyToManyField(curso)
    turmasEnvolvidas = models.ManyToManyField(turma)
    fotoEdicao = models.ImageField(upload_to='edicoes', null=True, blank=True)
    aceitaInscricoes = models.BooleanField(default=True, null=True, blank=True)
    prazoInscricoes = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.ano}.{self.semestre}'
    
    class Meta:
        verbose_name = 'Edição'
        verbose_name_plural = 'Edições'
        ordering = ['ano', 'semestre']

class aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=10)
    turma = models.ForeignKey(turma, on_delete=models.RESTRICT)
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

class equipe(models.Model):
    nome = models.CharField(max_length=100)
    alunos = models.ManyToManyField(aluno)
    edicao = models.ForeignKey(edicao, on_delete=models.RESTRICT)
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

class avaliador(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=15)
    portfolio = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Avaliador'
        verbose_name_plural = 'Avaliadores'
        ordering = ['nome']

class avaliador_edicao(models.Model):
    avaliador = models.ForeignKey(avaliador, on_delete=models.RESTRICT)
    edicao = models.ForeignKey(edicao, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.avaliador} - {self.edicao.ano}.{self.edicao.semestre}'
    
    class Meta:
        verbose_name = 'Avaliador da Edição'
        verbose_name_plural = 'Avaliadores das Edições'
        ordering = ['avaliador', 'edicao__ano', 'edicao__semestre']

class criterio(models.Model):
    descricao = models.TextField()
    peso = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name = 'Critério'
        verbose_name_plural = 'Critérios'
        ordering = ['descricao']

class edicao_criterio(models.Model):
    edicao = models.ForeignKey(edicao, on_delete=models.RESTRICT)
    criterio = models.ForeignKey(criterio, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.edicao.ano}.{self.edicao.semestre} - {self.criterio}'
    
    class Meta:
        verbose_name = 'Critério da Edição'
        verbose_name_plural = 'Critérios das Edições'
        ordering = ['edicao__ano', 'edicao__semestre', 'criterio']

class avaliacao(models.Model):
    avaliador = models.ForeignKey(avaliador, on_delete=models.RESTRICT)
    equipe = models.ForeignKey(equipe, on_delete=models.RESTRICT)
    criterio = models.ForeignKey(criterio, on_delete=models.RESTRICT)
    nota = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return f'{self.avaliador.nome} - {self.equipe.nome} - {self.criterio.descricao} - {self.nota}'

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'

class apoiadores(models.Model):
    empresa = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='apoiadores', null=True, blank=True)
    link = models.URLField()
    edicao = models.ForeignKey(edicao, on_delete=models.RESTRICT, null=True, blank=True)

    def __str__(self):
        return f'{self.empresa}'
    
    class Meta:
        verbose_name = 'Apoiador'
        verbose_name_plural = 'Apoiadores'
        ordering = ['empresa']

class ranking(models.Model):
    equipe = models.ForeignKey(equipe, on_delete=models.RESTRICT)
    notaFinal = models.DecimalField(max_digits=3, decimal_places=1)
    classificacao = models.IntegerField()
    edicao = models.ForeignKey(edicao, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.equipe.nome} - {self.notaFinal} - {self.classificacao}'
    
    class Meta:
        verbose_name = 'Ranking'
        verbose_name_plural = 'Rankings'
        ordering = ['edicao__ano', 'edicao__semestre', 'equipe__nome', 'classificacao']
