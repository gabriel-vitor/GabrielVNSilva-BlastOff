from django.contrib import admin
from escola.models import Aluno

# Register your models here.

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', )      #vai pesquisar só pelo nome


admin.site.register(Aluno, Alunos)