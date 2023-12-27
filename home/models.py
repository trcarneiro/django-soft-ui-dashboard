from django.db import models

# Create your models here.

class Bot(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(null=True, blank=True)

class Procedimento(models.Model):
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    ordem = models.IntegerField()

class Acao(models.Model):
    procedimento = models.ForeignKey(Procedimento, on_delete=models.CASCADE)
    tipo_acao = models.CharField(max_length=255)
    xpath = models.TextField()
    valor = models.TextField(null=True, blank=True)

