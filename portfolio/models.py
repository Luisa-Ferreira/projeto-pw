from django.db import models

class Luisa(models.Model):
    nome = models.CharField(max_length=100)
    apresentacao = models.TextField()
    foto = models.ImageField(null=True,blank=True,upload_to='bands')
    competencias = models.TextField()

    def __str__(self):
        return f'{self.nome}'