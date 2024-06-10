from django.db import models

class Musica(models.Model):
    nome = models.CharField(max_length=100)
    duracao = models.CharField(max_length=100)
    spotify = models.URLField(blank = True)
    letra = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return f'{self.nome}'

class Album(models.Model):
    titulo = models.CharField(max_length=100)
    ano_lancamento = models.IntegerField()
    data = models.DateField()
    capa = models.ImageField(null=True,blank=True,upload_to='bands/fotos')
    musicas = models.ManyToManyField(Musica,related_name='albuns')

    def __str__(self):
        return f'{self.titulo}'

class Banda(models.Model):

    nome = models.CharField(max_length=100)
    biografia= models.TextField(blank=True)
    nacionalidade = models.CharField(max_length=100,null=True)
    ano_criacao = models.IntegerField()
    fotoBanda = models.ImageField(null=True,blank=True,upload_to='bands')
    albuns =  models.ManyToManyField(Album,related_name='bandas')

    def __str__(self):
        return f'{self.nome}'













