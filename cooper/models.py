from unicodedata import name
from django.db import models
class Associados(models.Model):
    cpf = models.CharField(max_length=13, primary_key = True)
    nomeAssociado = models.CharField(max_length=100)
    quotas = models.IntegerField()
    nomeRespoAssociado = models.CharField(max_length=200)
    dt_nasct = models.DateField()
    cidadeNatal = models.CharField(max_length=50)
    estadoNatal = models.CharField(max_length=2)
    telefone = models.CharField(max_length=14)
    email = models.EmailField()
    rg = models.IntegerField()
    isAssociado = models.BooleanField()
    cargo = models.CharField(max_length=50)
    ##
    rua = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidadeAtual = models.CharField(max_length=50)
    cep = models.CharField(max_length=9)

class Users(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

def chk_table(reques1, reques2):
    name = reques1
    password = reques2
    if Users.objects.filter(name=name, password=password).exists():
        votes_table = Users.objects.filter(name=name, password=password).exists()
        print(votes_table)
    else:
        pass
    