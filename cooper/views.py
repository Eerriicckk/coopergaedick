from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

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
    response = redirect('/redirect-success/')
    return response