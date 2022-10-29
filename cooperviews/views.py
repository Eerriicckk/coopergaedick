from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib import messages
from django_tables2 import SingleTableView
from cooperviews.models import chk_table, chk_tabl, chkProj, createAssociado, createProj, Associados, Projetos
from .tables import PersonTable
from .forms import CreateAssociado, CheckCpf, UpdateAssociado, ProjetosInput, CheckCodigo
from .models import Associados

class PersonListView(SingleTableView):
    model = Associados
    tables_class = PersonTable
    template_name = 'accounts/ver_associados_page.html'

def view_info(request):
    if request.user.is_authenticated:
        objs=Associados.objects.all()
        return render(request, 'accounts/ver_associados_page.html', {'objs':objs})
    else:
        messages.add_message(request, messages.INFO, 'Você não está logado')
        return render(request, 'accounts/notloggedwarning.html')

def sortViewAssociados(request, sort):
    if request.user.is_authenticated:
        objs=Associados.objects.all().order_by(sort)
        return render(request, 'accounts/ver_associados_page.html', {'objs':objs})
    else:
        messages.add_message(request, messages.INFO, 'Você não está logado')
        return render(request, 'accounts/notloggedwarning.html')

def viewProjects(request):
    if request.user.is_authenticated:
        objs=Projetos.objects.all().order_by('-projConcluido')
        return render(request, 'accounts/verProjetosPage.html', {'objs':objs})
    else:
        messages.add_message(request, messages.INFO, 'Você não está logado')
        return render(request, 'accounts/notloggedwarning.html')

def sortViewProjects(request, sort):
    if request.user.is_authenticated:
        objs=Projetos.objects.all().order_by(sort)
        return render(request, 'accounts/verProjetosPage.html', {'objs':objs})
    else:
        messages.add_message(request, messages.INFO, 'Você não está logado')
        return render(request, 'accounts/notloggedwarning.html')

def principal(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/principalpage.html')
    else:
        messages.add_message(request, messages.INFO, 'Você não está logado')
        return render(request, 'accounts/notloggedwarning.html')

def cadastrar(request):
    if request.user.is_authenticated:
        context = {}
        context['form'] = CreateAssociado()
        return render(request, 'accounts/cadastrarpage.html', context)
    else:
        messages.add_message(request, messages.INFO, 'Você não está logado')
        return render(request, 'accounts/notloggedwarning.html')

def cadastrarProjeto(request):
    if request.user.is_authenticated:
        context = {}
        context['form'] = ProjetosInput()
        return render(request, 'accounts/criarprojetospage.html', context)
    else:
        messages.add_message(request, messages.INFO, 'Você não está logado')
        return render(request, 'accounts/notloggedwarning.html')

def gerenciarAssociado(request):
    if request.user.is_authenticated:
        context = {}
        context['form'] = CheckCpf()
        return render(request, 'accounts/gerenciarassociados_page.html', context)
    else:
        messages.add_message(request, messages.INFO, 'Você não está logado')
        return render(request, 'accounts/notloggedwarning.html')

def gerenciarProjeto(request):
    if request.user.is_authenticated:
        context = {}
        context['form'] = CheckCodigo()
        return render(request, 'accounts/checarProjetosPage.html', context)
    else:
        messages.add_message(request, messages.INFO, 'Você não está logado')
        return render(request, 'accounts/notloggedwarning.html')

def login(request):
    if request.user.is_authenticated:
        print("logged")
    else:
        print("not logged")
    return render(request, 'registration/login22.html')

def redirect_view(request):
    context = {}
    login_data = request.POST.dict()
    user = login_data.get("user")
    senha = login_data.get("password")

    check = chk_table(user, senha)
    if check == True:
        response = render(request, 'accounts/principalpage.html')
    else:
        response = render(request, 'registration/login.html', context)
    return response

def createUser(request):
    print("createUser")
    login_data = request.POST.dict()

    cpf= login_data.get("cpf")
    nomeAssociado= login_data.get("nome")
    quotas= login_data.get("quotas")
    nomeRespoAssociado= login_data.get("nomeresponsavel")
    dt_nasct= login_data.get("datadenascimento")
    cidadeNatal= login_data.get("cidadenatal")
    estadoNatal= login_data.get("estadonatal")
    estadoNatal = estadoNatal.upper()
    telefone= login_data.get("telefone")
    email= login_data.get("email")
    email = email.lower()
    rg= login_data.get("rg")
    isAssociado= login_data.get("associado")
    if isAssociado == "on":
        isAssociado = True
    else:
        isAssociado = False
    cargo= login_data.get("cargo")
    cargo = cargo.title()
    rua= login_data.get("rua")
    rua = rua.title()
    bairro= login_data.get("bairro")
    bairro = bairro.title()
    cidadeAtual= login_data.get("cidade")
    cidadeAtual = cidadeAtual.title()
    cep= login_data.get("cep")
    associado = createAssociado(cpf, nomeAssociado, quotas, nomeRespoAssociado, dt_nasct, cidadeNatal, estadoNatal, telefone, email, rg, isAssociado, cargo, rua, bairro, cidadeAtual, cep)
    print(associado)
    response = render(request, 'accounts/successpage.html')
    return response

def createProjeto(request):
    print("createProj")
    login_data = request.POST.dict()
    nomeProj= login_data.get("nomeProjeto")
    descrProj= login_data.get("descricaoProjeto")
    projConcluido= login_data.get("isConcluido")
    print(projConcluido)
    if projConcluido == "on":
        projConcluido = True
    else:
        projConcluido = False
    print("concluido", projConcluido)
    projeto = createProj(nomeProj, descrProj, projConcluido)
    print(projeto)
    mensagem = "Código do projeto: "+str(projeto)
    messages.add_message(request, messages.INFO, mensagem)
    response = render(request, 'accounts/successpageproj.html')
    return response

def checkCpf(request): #checa o cpf e já adiciona as informacoes nos campos necessarios da proxima pagina
    if request.user.is_authenticated:
        login_data = request.POST.dict()
        cpf = login_data.get("cpf")
        check = chk_tabl(cpf)
        if check == True:
            data = Associados.objects.get(cpf=cpf)
            initial_data = {
                'cpf' : data.cpf,
                'nome' : data.nomeAssociado,
                'quotas' : data.quotas,
                'nomeresponsavel' : data.nomeRespoAssociado,
                'datadenascimento' : data.dt_nasct,
                'cidadenatal' : data.cidadeNatal,
                'estadonatal' : data.estadoNatal,
                'telefone' : data.telefone,
                'email' : data.email,
                'rg' : data.rg,
                'associado' : data.isAssociado,
                'cargo' : data.cargo,
                'rua' : data.rua,
                'bairro' : data.bairro, 
                'cidade' : data.cidadeAtual,
                'cep' : data.cep
            }
            form = UpdateAssociado(initial=initial_data)
            context = {
                'data': data,
                'form': form
            }
            response = render(request, 'accounts/gerenciarapage.html', context)
            return response
        else:
            context = {}
            context['form'] = CheckCpf()
            messages.add_message(request, messages.INFO, 'Associado não encontrado!')
            return render(request, 'accounts/gerenciarassociados_page.html', context)
    else:
        messages.add_message(request, messages.INFO, 'Você não está logado')
        return render(request, 'accounts/notloggedwarning.html')

def checkProject(request): #checa o codigo do projeto e já adiciona as informacoes nos campos necessarios da proxima pagina
    if request.user.is_authenticated:
        login_data = request.POST.dict()
        cpf = login_data.get("codProjeto")
        check = chkProj(cpf)
        if check == True:
            data = Projetos.objects.get(codProjeto=cpf)
            initial_data = {
                'nomeProjeto' : data.nomeProjeto,
                'descricaoProjeto' : data.descricaoProjeto,
                'isConcluido' : data.projConcluido,
                'codProjeto' : data.codProjeto,
                'dtCriacao' : data.dtCriacao,
                'hiddenCodProjeto' : data.codProjeto
            }
            form = ProjetosInput(initial=initial_data)
            context = {
                'data': data,
                'form': form
            }
            response = render(request, 'accounts/gerenciarProjetosPage.html', context)
            return response
        else:
            context = {}
            context['form'] = CheckCodigo()
            messages.add_message(request, messages.INFO, 'Código incorreto')
            return render(request, 'accounts/checarProjetosPage.html', context)
    else:
        messages.add_message(request, messages.INFO, 'Você não está logado')
        return render(request, 'accounts/notloggedwarning.html')

def updateAssociado(request):
    print("updateAsso")
    login_data = request.POST.dict()
    print("1")
    cpf= login_data.get("cpf")
    nomeAssociado= login_data.get("nome")
    quotas= login_data.get("quotas")
    nomeRespoAssociado= login_data.get("nomeresponsavel")
    dt_nasct= login_data.get("datadenascimento")
    cidadeNatal= login_data.get("cidadenatal")
    estadoNatal= login_data.get("estadonatal")
    estadoNatal = estadoNatal.upper()
    telefone= login_data.get("telefone")
    email= login_data.get("email")
    email = email.lower()
    rg= login_data.get("rg")
    isAssociado= login_data.get("associado")
    if isAssociado == "on":
        isAssociado = True
    else:
        isAssociado = False
    cargo= login_data.get("cargo")
    cargo = cargo.title()
    rua= login_data.get("rua")
    rua = rua.title()
    bairro= login_data.get("bairro")
    bairro = bairro.title()
    cidadeAtual= login_data.get("cidade")
    cidadeAtual = cidadeAtual.title()
    cep= login_data.get("cep")
    associados = Associados(cpf=cpf, nomeAssociado=nomeAssociado, quotas=quotas, nomeRespoAssociado=nomeRespoAssociado, dt_nasct=dt_nasct, cidadeNatal=cidadeNatal, estadoNatal=estadoNatal, telefone=telefone, email=email, rg=rg, isAssociado=isAssociado, cargo=cargo, rua=rua, bairro=bairro, cidadeAtual=cidadeAtual, cep=cep)
    associados.save()
    print("associados")
    response = render(request, 'accounts/successpage.html')
    return response

def updateProjeto(request):
    print("createProjet")
    login_data = request.POST.dict()
    nomeProj= login_data.get("nomeProjeto")
    descrProj= login_data.get("descricaoProjeto")
    projConcluido= login_data.get("isConcluido")
    codProjeto = login_data.get("codProjeto")
    dtCriacao = login_data.get("dtCriacao")
    print(projConcluido)
    if projConcluido == "on":
        projConcluido = True
    else:
        projConcluido = False
    print("concluido", projConcluido)
    projeto = Projetos(codProjeto=codProjeto, dtCriacao=dtCriacao, nomeProjeto=nomeProj, descricaoProjeto=descrProj, projConcluido=projConcluido)
    projeto.save()
    response = render(request, 'accounts/successpageproj.html')
    return response

def logutView(request):
    logout(request)

def deleteProj(request):
    login_data = request.POST.dict()
    codProjeto = login_data.get("hiddenCodProjeto")
    print(codProjeto)
    projeto = Projetos.objects.get(codProjeto=codProjeto)
    projeto.delete()
    response = render(request, 'accounts/principalpage.html')
    return response
# Create your views here.
