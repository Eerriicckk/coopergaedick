from django.db import models
import random, datetime

class Associados(models.Model):
    cpf = models.PositiveBigIntegerField(primary_key = True)
    nomeAssociado = models.CharField(max_length=100)
    quotas = models.IntegerField()
    nomeRespoAssociado = models.CharField(max_length=200)
    dt_nasct = models.DateField()
    cidadeNatal = models.CharField(max_length=50)
    estadoNatal = models.CharField(max_length=2)
    telefone = models.PositiveBigIntegerField()
    email = models.EmailField()
    rg = models.PositiveBigIntegerField()
    isAssociado = models.BooleanField()
    cargo = models.CharField(max_length=50)
    ##
    rua = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidadeAtual = models.CharField(max_length=50)
    cep = models.PositiveBigIntegerField()

class Users(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

class Projetos(models.Model):
    codProjeto = models.PositiveIntegerField(primary_key = True)
    dtCriacao = models.DateField()
    nomeProjeto = models.CharField(max_length=140)
    descricaoProjeto = models.TextField(max_length=500)
    projConcluido = models.BooleanField()

def chk_table(reques1, reques2):
    name = reques1
    password = reques2
    if Users.objects.filter(name=name, password=password).exists():
        votes_table = Users.objects.filter(name=name, password=password).exists()
        print(votes_table)
        return votes_table

def createProj(nOMEPROJETO, dESCRICAOPROJETO, pROJCONCLUIDO):
    codProjeto = random.randint(1000000000, 2147483600)
    data = datetime.datetime.now()
    dtCriacao = str(data.year)+"-"+str(data.month)+"-"+str(data.day)
    nomeProjeto = nOMEPROJETO
    descricaoProjeto = dESCRICAOPROJETO
    projConcluido = pROJCONCLUIDO
    print("is concluido",projConcluido)
    esta = True
    while esta:
        numero = random.randint(1000000000, 2147483600)
        if Projetos.objects.filter(codProjeto=numero).exists():
            esta = True
        else:
            esta = False
            break
    Projetos.objects.create(codProjeto=codProjeto,dtCriacao=dtCriacao,nomeProjeto=nomeProjeto, descricaoProjeto=descricaoProjeto, projConcluido=projConcluido)
    print("gravou")
    return codProjeto
    
def createAssociado(cPF, nOMEASSOCIADO, qUOTAS, nOMERESPOASSOCIADO, dT_nASCT, cIDADENATAL, eSTADONATAL, tELEFONE, eMAIL, rG, iSASSOCIADO, cARGO, rUA, bAIRRO, cIDADEATUAL, cEP):
    cpf =cPF
    nomeAssociado =nOMEASSOCIADO
    quotas =qUOTAS
    nomeRespoAssociado =nOMERESPOASSOCIADO 
    dt_nasct =dT_nASCT
    cidadeNatal =cIDADENATAL
    estadoNatal =eSTADONATAL
    telefone =tELEFONE
    email =eMAIL
    rg =rG
    isAssociado =iSASSOCIADO
    cargo =cARGO
    rua =rUA
    bairro =bAIRRO
    cidadeAtual =cIDADEATUAL
    cep =cEP
    if isAssociado == 'on':
        isAssociado = True
    elif isAssociado == 'off':
        isAssociado = False
    if Associados.objects.filter(cpf=cpf).exists():
        checkPrimaryKey = Associados.objects.filter(cpf=cpf).exists()
        print(checkPrimaryKey)
        print("nao gravou")
        return checkPrimaryKey
    else:
        Associados.objects.create(cpf=cpf, nomeAssociado=nomeAssociado, quotas=quotas, nomeRespoAssociado=nomeRespoAssociado, dt_nasct=dt_nasct, cidadeNatal=cidadeNatal, estadoNatal=estadoNatal, telefone=telefone, email=email, rg=rg, isAssociado=isAssociado, cargo=cargo, rua=rua, bairro=bairro, cidadeAtual=cidadeAtual, cep=cep)
        print("gravou")

def updateAssociado(cPF, nOMEASSOCIADO, qUOTAS, nOMERESPOASSOCIADO, dT_nASCT, cIDADENATAL, eSTADONATAL, tELEFONE, eMAIL, rG, iSASSOCIADO, cARGO, rUA, bAIRRO, cIDADEATUAL, cEP):
    cpf =cPF
    nomeAssociado =nOMEASSOCIADO
    quotas =qUOTAS
    nomeRespoAssociado =nOMERESPOASSOCIADO 
    dt_nasct =dT_nASCT
    cidadeNatal =cIDADENATAL
    estadoNatal =eSTADONATAL
    telefone =tELEFONE
    email =eMAIL
    rg =rG
    isAssociado =iSASSOCIADO
    cargo =cARGO
    rua =rUA
    bairro =bAIRRO
    cidadeAtual =cIDADEATUAL
    cep =cEP
    if isAssociado == 'on':
        isAssociado = True
    elif isAssociado == 'off':
        isAssociado = False
    if Associados.objects.filter(cpf=cpf).exists():
        checkPrimaryKey = Associados.objects.filter(cpf=cpf).exists()
        print(checkPrimaryKey)
        print("nao gravou")
        return checkPrimaryKey
    else:
        Associados.objects.create(cpf=cpf, nomeAssociado=nomeAssociado, quotas=quotas, nomeRespoAssociado=nomeRespoAssociado, dt_nasct=dt_nasct, cidadeNatal=cidadeNatal, estadoNatal=estadoNatal, telefone=telefone, email=email, rg=rg, isAssociado=isAssociado, cargo=cargo, rua=rua, bairro=bairro, cidadeAtual=cidadeAtual, cep=cep)
        print("gravou")

def filterAssociado(cPF, nOMEASSOCIADO, qUOTAS, nOMERESPOASSOCIADO, dT_nASCT, cIDADENATAL, eSTADONATAL, tELEFONE, eMAIL, rG, iSASSOCIADO, cARGO, rUA, bAIRRO, cIDADEATUAL, cEP, dECRESCENTE):
    cpf =cPF
    nomeAssociado =nOMEASSOCIADO
    quotas =qUOTAS
    nomeRespoAssociado =nOMERESPOASSOCIADO 
    dt_nasct =dT_nASCT
    cidadeNatal =cIDADENATAL
    estadoNatal =eSTADONATAL
    telefone =tELEFONE
    email =eMAIL
    rg =rG
    isAssociado =iSASSOCIADO
    cargo =cARGO
    rua =rUA
    bairro =bAIRRO
    cidadeAtual =cIDADEATUAL
    cep =cEP
    decrescente = dECRESCENTE
    if isAssociado == 'on':
        isAssociado = True
    elif isAssociado == 'off':
        isAssociado = False
    
        checkPrimaryKey = Associados.objects.filter(cpf=cpf).exists()
        print(checkPrimaryKey)
        print("nao gravou")
        return checkPrimaryKey

def checkCpf(data):
    cPF = data
    if Associados.objects.filter(cpf=cPF).exists():
        print("ok")

def chk_tabl(reques1):
    cpf = reques1
    if Associados.objects.filter(cpf=cpf).exists():
        votes_table = Associados.objects.filter(cpf=cpf).exists()
        return votes_table
    votes_table = Associados.objects.filter(cpf=cpf).exists()
    return votes_table
# Create your models here.
