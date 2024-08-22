from django.contrib import admin
from .models import DadosBasicos


class PessoasAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'nome')


admin.site.register(DadosBasicos, PessoasAdmin)
