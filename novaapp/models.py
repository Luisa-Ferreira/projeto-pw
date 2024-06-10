from django.db import models

class Consequencia(models.Model):
    consequencia = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.consequencia}'

class Verdade(models.Model):
    verdade = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.verdade}'