from django.db import models
from datetime import date


# Create your models here.
class Exercicio(models.Model):
    id = models.AutoField(primary_key = True)
    nome = models.CharField(max_length = 250)
    descricao = models.CharField(max_length = 500)
    em_equipamento = models.BooleanField(default = True)
    idade_minima_aluno = models.PositiveIntegerField(default = 12)

    class Meta:
        verbose_name = 'Exercício'
        verbose_name_plural = 'Exercícios'


class Alunos(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length = 250)
    foto = models.ImageField(null = True, blank =  True)
    sexo_choices = (('M', 'Masculino'), ('F', 'Feminino'))
    sexo = models.CharField(max_length = 1, choices = sexo_choices)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length = 20)
    cpf = models.CharField(max_length = 14)

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
    
    def idade(self):
        hoje = date.today()
        idade = hoje.year - self.data_nascimento.year - ((hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day))
        return idade
    
    def __str__(self):
        return f'Nome: {self.nome} | Idade: {self.data_nascimento}'

