from django.db import models

class Banda(models.Model):

    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=100,null=True)
    ano_criacao = models.IntegerField()


    def __str__(self):
        return f'{self.nome}'

class Festival(models.Model):
    nome = models.CharField(max_length=100)
    anoRealizacao = models.IntegerField()
    bandas = models.ManyToManyField(Banda,related_name='festival')
    fotoFestival = models.ImageField(null=True,blank=True,upload_to='bands')

    def __str__(self):
        return f'{self.nome}'

class Localizacao(models.Model):

    nome = models.CharField(max_length=100)
    anoRealizacao = models.IntegerField()
    festivais = models.ManyToManyField(Festival,related_name='localizacao')

    def __str__(self):
        return f'{self.nome}'