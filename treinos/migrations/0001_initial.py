# Generated by Django 3.2.12 on 2024-03-31 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alunos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1)),
                ('data_nascimento', models.DateField()),
                ('telefone', models.CharField(max_length=20)),
                ('cpf', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='Exercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('descricao', models.CharField(max_length=500)),
                ('em_equipamento', models.BooleanField(default=True)),
                ('idade_minima_aluno', models.PositiveIntegerField(default=12)),
            ],
        ),
    ]
