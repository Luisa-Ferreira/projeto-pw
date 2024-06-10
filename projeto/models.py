from django.db import models

class Docente(models.Model):
    nomeDocente = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    apresentacao = models.TextField()
    objetivos = models.TextField()
    competencias = models.TextField()
    docenteCurso = models.ManyToManyField(Docente,related_name='curso')

    def __str__(self):
        return f'{self.nome}'


class Area_Cientifica(models.Model):
    nomeArea = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.nomeArea}'

class LinguagemProgramacao(models.Model):
    linguagem = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.linguagem}'

class Projeto(models.Model):
    linguagem = models.ManyToManyField(LinguagemProgramacao,related_name='projetos')

    nome = models.CharField(max_length=100)
    descricao=models.CharField(max_length=1000)
    descricaoLonga = models.TextField()
    conceitosAplicados = models.TextField()
    tecnologiasUsadas = models.CharField(max_length=100)
    imagem = models.ImageField(null=True,blank=True,upload_to='bands')
    linkVideo = models.URLField(max_length=200, blank=True)
    linkGithub = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f'{self.nome}'


class Disciplina(models.Model):
    linguagem= models.ManyToManyField(LinguagemProgramacao,related_name='disciplinas')
    docentes= models.ManyToManyField(Docente,related_name='disciplinas')
    projeto= models.OneToOneField(Projeto,on_delete=models.CASCADE,related_name='disciplinas',null=True)
    areaCientifica= models.ForeignKey(Area_Cientifica, on_delete=models.CASCADE,related_name='disciplina')
    cursos= models.ManyToManyField(Curso,related_name='disciplinas')

    nomeDisciplina = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()
    curricularIUnitReadableCode = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nomeDisciplina}'


