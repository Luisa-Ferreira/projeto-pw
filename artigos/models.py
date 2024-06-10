from django.db import models
from django.contrib.auth.models import User

class Autor(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='artigos')
    foto = models.ImageField(default='defaultUser.jpg')
    username= models.CharField(max_length=100)
    VERY_BAD = 0
    BAD = 1
    OK = 2
    GOOD = 3
    VERY_GOOD = 4

    RATING_CHOICES = [
        (VERY_BAD, "0"),
        (BAD, "1"),
        (OK, "2"),
        (GOOD, "3"),
        (VERY_GOOD, "4"),
    ]

    rating = models.PositiveIntegerField(choices=RATING_CHOICES, default=OK)

    def __str__(self):
        return f'{self.username}'

class Comentario(models.Model):
    autor= models.ForeignKey(Autor, on_delete=models.CASCADE,related_name='comentarios')
    mensagem= models.CharField(max_length=10000)

    def __str__(self):
        return f'{self.autor} - {self.mensagem}'


class Artigo(models.Model):
    autor= models.ForeignKey(Autor, on_delete=models.CASCADE,related_name='artigos')
    data = models.DateField()
    titulo = models.CharField(max_length=100)
    cabecaNoticia = models.TextField()
    noticia = models.TextField()
    foto = models.ImageField(default='default.jpg')
    comentarios = models.ManyToManyField(Comentario, related_name='artigos')


    def __str__(self):
        return f'{self.titulo}'