from unittest.util import _MAX_LENGTH
from django import forms
from django.forms import NumberInput, PasswordInput, Textarea

class DateInput(forms.DateInput):
    input_type = 'date'

class ProjetosInput(forms.Form):
    nomeProjeto = forms.CharField(max_length=140)
    descricaoProjeto = forms.CharField(max_length=500, widget=Textarea)
    isConcluido = forms.BooleanField(required=False)
    dtCriacao = forms.DateField(widget=DateInput(attrs={'readonly':'readonly'}))
    codProjeto = forms.IntegerField(widget=NumberInput(attrs={'readonly':'readonly', 'pattern': '[0-9]{10}', 'type': 'text'}))
    hiddenCodProjeto = forms.IntegerField(widget=NumberInput(attrs={'type':'hidden'}))

class CreateAssociado(forms.Form):
    cpf = forms.IntegerField(max_value=99999999999, widget=NumberInput(attrs={'placeholder': 'Ex: 20711247072', 'pattern': '[0-9]{11}', 'type': 'text'}))
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ex: Daiane Pietra Barbosa'}))
    quotas = forms.IntegerField(widget=NumberInput(attrs={'placeholder': 'Ex: 1'}))
    nomeresponsavel = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Ex: Marcela Ayla Benedita'}))
    datadenascimento = forms.DateField(widget=DateInput)
    cidadenatal = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ex: Manaus'}))
    estadonatal = forms.CharField(max_length=2, widget=forms.TextInput(attrs={'placeholder': 'Ex: AM', 'pattern': '[A-Za-z]{2}', 'type': 'text'}))
    telefone = forms.IntegerField(max_value=99999999999, widget=forms.NumberInput(attrs={'placeholder': 'EX: 54912345678', 'pattern': '[0-9]{11}', 'type': 'text'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Ex: daianebarbosa@gmail.com.br'}))
    rg = forms.IntegerField(max_value=999999999, widget=NumberInput(attrs={'placeholder': 'Ex: 405435800', 'pattern': '[0-9]{9}', 'type': 'text'}))
    associado = forms.BooleanField(required=False)
    cargo = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ex: Conselho Fiscal'}))
    rua = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ex: Rua Raul Zagury'}))
    bairro = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ex: São Francisco'}))
    cidade = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ex: Manaus'}))
    cep = forms.IntegerField(max_value=99999999, widget=NumberInput(attrs={'placeholder': 'Ex: 69079050', 'pattern': '[0-9]{8}', 'type': 'text'}))

class UpdateAssociado(forms.Form):
    cpf = forms.IntegerField(max_value=99999999999, widget=NumberInput(attrs={'placeholder': 'Ex: 20711247072', 'readonly':'readonly', 'pattern': '[0-9]{11}', 'type': 'text'}))
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ex: Daiane Pietra Barbosa'}))
    quotas = forms.IntegerField(widget=NumberInput(attrs={'placeholder': 'Ex: 1'}))
    nomeresponsavel = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Ex: Marcela Ayla Benedita'}))
    datadenascimento = forms.DateField(widget=DateInput)
    cidadenatal = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ex: Manaus'}))
    estadonatal = forms.CharField(max_length=2, widget=forms.TextInput(attrs={'placeholder': 'Ex: AM', 'pattern': '[A-Za-z]{2}', 'type': 'text'}))
    telefone = forms.IntegerField(max_value=99999999999, widget=forms.NumberInput(attrs={'placeholder': 'EX: 54912345678', 'pattern': '[0-9]{11}', 'type': 'text'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Ex: daianebarbosa@gmail.com.br'}))
    rg = forms.IntegerField(max_value=999999999, widget=NumberInput(attrs={'placeholder': 'Ex: 405435800', 'pattern': '[0-9]{9}', 'type': 'text'}))
    associado = forms.BooleanField(required=False)
    cargo = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ex: Conselho Fiscal'}))
    rua = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ex: Rua Raul Zagury'}))
    bairro = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ex: São Francisco'}))
    cidade = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ex: Manaus'}))
    cep = forms.IntegerField(max_value=99999999, widget=NumberInput(attrs={'placeholder': 'Ex: 69079050', 'pattern': '[0-9]{8}', 'type': 'text'}))

class CheckCpf(forms.Form):
    cpf = forms.IntegerField(max_value=99999999999, widget=NumberInput(attrs={'pattern': '[0-9]{11}', 'type': 'text'}))
    

class CheckCodigo(forms.Form):
    codProjeto = forms.IntegerField(max_value=99999999999, widget=NumberInput(attrs={'pattern': '[0-9]{10}', 'type': 'text'}))
    

class FilterOptions(forms.Form):
    nome = forms.BooleanField(required=False)
    quotas = forms.BooleanField(required=False)
    nomeresponsavel = forms.BooleanField(required=False)
    datadenascimento = forms.BooleanField(required=False)
    cidadenatal = forms.BooleanField(required=False)
    estadonatal = forms.BooleanField(required=False)
    telefone = forms.BooleanField(required=False)
    email = forms.BooleanField(required=False)
    rg = forms.BooleanField(required=False)
    associado = forms.BooleanField(required=False)
    cargo = forms.BooleanField(required=False)
    rua = forms.BooleanField(required=False)
    bairro = forms.BooleanField(required=False)
    cidade = forms.BooleanField(required=False)
    cep = forms.BooleanField(required=False)
    decrescente = forms.BooleanField(required=False)