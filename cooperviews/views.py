from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from cooperviews.models import chk_table, createAssociado
from cooper.forms import NameForm

def home(request):
    return HttpResponse('Home page')

def principal(request):
    return render(request, 'accounts/principalpage.html')

def cadastrar(request):
    return render(request, 'accounts/cadastrarpage.html')

def gerenciar(request):
    return render(request, 'accounts/gerenciarassociados_page.html')

def login(request):
    return render(request, 'registration/login.html')

def redirect_view(request):
    user = request.POST['usuario']
    senha = request.POST['senha']
    check = chk_table(user, senha)
    if check == True:
        response = render(request, 'accounts/principalpage.html')
    else:
        response = render(request, 'registration/login.html')
    return response

def createUser(request):
    cpf= request.POST['cpf']
    associado = createAssociado(cpf)
    print(associado)
    response = render(request, 'registration/login.html')
    return response


# Create your views here.
