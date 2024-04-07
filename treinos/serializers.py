from rest_framework import serializers
from .models import Exercicio, Alunos

class ExercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercicio
        #fields = '__all__'
        fields = ['id', 'nome', 'descricao', 'em_equipamento', 'idade_minima_aluno']

class AlunosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alunos
        #fields = '__all__'
        fields = ['id', 'nome', 'foto', 'sexo', 'data_nascimento', 'telefone', 'cpf']
