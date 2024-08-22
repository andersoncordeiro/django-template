from django.db import models


class DadosBasicos(models.Model):
    nome             = models.CharField(max_length=200)
    cpf              = models.CharField(max_length=15, blank=True, null=True)
    telefone         = models.CharField(max_length=20, blank=True, null=True)
    nascimento       = models.DateField(blank=True, null=True)
    ativo            = models.BooleanField(default=True, verbose_name='Ativo')
    
    class Meta:
        verbose_name_plural = 'dados'
