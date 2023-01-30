from django.contrib import admin

from .models import Cargo, Servico, Funcionario, RecursosEsquerdo, RecursosDireito, Preco

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')

@admin.register(RecursosEsquerdo)
class RecrusosAdmin(admin.ModelAdmin):
    list_display = ('tecnologia', 'descricao', 'icone')

@admin.register(RecursosDireito)
class RecrusosAdmin(admin.ModelAdmin):
    list_display = ('tecnologia', 'descricao', 'icone')

@admin.register(Preco)
class PrecosAdmin(admin.ModelAdmin):
    list_display = ('icone', 'preco', 'qts_usuarios', 'capacidade', 'email_suporte', 'atualizacoes')
