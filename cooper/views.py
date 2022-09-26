from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from cooper.models import chk_table
from .forms import NameForm

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
    chk_table("user", "senha")
    return render(request, 'registration/login.html')
    '''response = redirect('/redirect-success/')
    return response'''

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
