from django.contrib import admin
from .models import Exercicio, Alunos

class ExercicioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'em_equipamento', 'idade_minima_aluno')
    list_filter = ('em_equipamento',)
    search_fields = ('nome', 'descricao')

class AlunosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'sexo', 'data_nascimento', 'telefone', 'cpf')
    list_filter = ('sexo',)
    search_fields = ('nome', 'cpf')

    def idade(self, obj):
        return obj.idade()
    idade.short_description = 'Idade'

admin.site.register(Exercicio, ExercicioAdmin)
admin.site.register(Alunos, AlunosAdmin)

admin.site.site_header = "ERICKY ACADEMIA"
#admin.site.site_title = ""
