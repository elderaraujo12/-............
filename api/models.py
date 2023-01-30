from django.db import models
from django.utils import timezone

# Create your models here.

class Sobrevivente(models.Model):
    nome = models.CharField(max_length=1001
    )
    idade = models.CharField(max_length=4)
    sexo = models.CharField(max_length= 15)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    relatorio_de_saude = models.TextField(blank=True, null=True)



    class meta:
        db_table = 'sobrevivente'

class Recursos(models.Model):
    propriedade = models.CharField(max_length=100)
    descricao = models.CharField(max_length=400)

    class meta:
        db_table = 'Recursos'

class Itens(models.Model):
    nome = models.CharField(max_length=100)
    pontos = models.CharField(max_length=5)
    descricao = models.CharField(max_length=400)

    class meta:
        db_table = 'Itens'


class Infectado(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=400)

    class meta:
        db_table = 'Infectado'


class Trocas(models.Model):
    agua = models.CharField(max_length=10)
    alimentos = models.CharField(max_length=30)
    medicacao = models.CharField(max_length=30)
    municao = models.CharField(max_length=30)

    pontos_agua = models.CharField(max_length=10)
    pontos_alimento = models.CharField(max_length=10)
    pontos_medicacao = models.CharField(max_length=10)
    pontos_municao = models.CharField(max_length=10)

    class meta:
        db_table = 'Tocas'

