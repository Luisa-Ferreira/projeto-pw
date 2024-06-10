from django.db import models

class Pessoa(models.Model):
    nome=models.CharField(max_length=100)
    idade= models.IntegerField()
    morada=models.CharField(max_length=100)
    dataDeNascimento = models.DateField()

    def __str__(self):
        return f'{self.nome} - {self.idade} anos'