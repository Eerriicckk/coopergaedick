from django import forms
from django.forms import NumberInput, PasswordInput

class DateInput(forms.DateInput):
    input_type = 'date'

class CheckUser(forms.Form):
    user = forms.CharField()
    password = forms.CharField(widget=PasswordInput)

class CreateAssociado(forms.Form):
    cpf = forms.IntegerField(max_value=99999999999, widget=NumberInput(attrs={'placeholder': 'Ex: 20711247072'}))
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ex: Daiane Pietra Barbosa'}))
    quotas = forms.IntegerField(widget=NumberInput(attrs={'placeholder': 'Ex: 1'}))
    nomeresponsavel = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Ex: Marcela Ayla Benedita'}))
    datadenascimento = forms.DateField(widget=DateInput)
    cidadenatal = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ex: Manaus'}))
    estadonatal = forms.CharField(max_length=2, widget=forms.TextInput(attrs={'placeholder': 'Ex: AM'}))
    telefone = forms.IntegerField(max_value=99999999999, widget=forms.NumberInput(attrs={'placeholder': 'EX: 54912345678'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Ex: daianebarbosa@gmail.com.br'}))
    rg = forms.IntegerField(max_value=999999999, widget=NumberInput(attrs={'placeholder': 'Ex: 405435800', 'pattern': '{9}'}))
    associado = forms.BooleanField(required=False)
    cargo = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ex: Conselho Fiscal'}))
    rua = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ex: Rua Raul Zagury'}))
    bairro = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ex: São Francisco'}))
    cidade = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ex: Manaus'}))
    cep = forms.IntegerField(max_value=99999999, widget=NumberInput(attrs={'placeholder': 'Ex: 69079050'}))

class UpdateAssociado(forms.Form):
    cpf = forms.IntegerField(max_value=99999999999, widget=NumberInput(attrs={'placeholder': 'Ex: 20711247072', 'readonly':'readonly'}))
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ex: Daiane Pietra Barbosa'}))
    quotas = forms.IntegerField(widget=NumberInput(attrs={'placeholder': 'Ex: 1'}))
    nomeresponsavel = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Ex: Marcela Ayla Benedita'}))
    datadenascimento = forms.DateField(widget=DateInput)
    cidadenatal = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ex: Manaus'}))
    estadonatal = forms.CharField(max_length=2, widget=forms.TextInput(attrs={'placeholder': 'Ex: AM'}))
    telefone = forms.IntegerField(max_value=99999999999, widget=forms.NumberInput(attrs={'placeholder': 'EX: 54912345678'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Ex: daianebarbosa@gmail.com.br'}))
    rg = forms.IntegerField(max_value=999999999, widget=NumberInput(attrs={'placeholder': 'Ex: 405435800', 'pattern': '{9}'}))
    associado = forms.BooleanField(required=False)
    cargo = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ex: Conselho Fiscal'}))
    rua = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ex: Rua Raul Zagury'}))
    bairro = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ex: São Francisco'}))
    cidade = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ex: Manaus'}))
    cep = forms.IntegerField(max_value=99999999, widget=NumberInput(attrs={'placeholder': 'Ex: 69079050'}))

class CheckCpf(forms.Form):
    cpf = forms.CharField()
