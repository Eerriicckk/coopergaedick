# Generated by Django 3.2.15 on 2022-09-28 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Associados',
            fields=[
                ('cpf', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('nomeAssociado', models.CharField(max_length=100)),
                ('quotas', models.IntegerField()),
                ('nomeRespoAssociado', models.CharField(max_length=200)),
                ('dt_nasct', models.DateField()),
                ('cidadeNatal', models.CharField(max_length=50)),
                ('estadoNatal', models.CharField(max_length=2)),
                ('telefone', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=254)),
                ('rg', models.IntegerField()),
                ('isAssociado', models.BooleanField()),
                ('cargo', models.CharField(max_length=50)),
                ('rua', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('cidadeAtual', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Projetos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_projeto', models.CharField(max_length=50)),
                ('data_projeto', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
