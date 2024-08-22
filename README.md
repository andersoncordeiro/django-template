# Django - Template de Projeto


## Iniciando um projeto Django

```bash
$ pip install django
$ django-admin startproject miniframework
$ cd miniframework
$ python manage.py startapp pessoas
```

## Editando `pessoas/models.py`

```python
from django.db import models


class DadosBasicos(models.Model):
    nome             = models.CharField(max_length=200)
    cpf              = models.CharField(max_length=15, blank=True, null=True)
    telefone         = models.CharField(max_length=20, blank=True, null=True)
    nascimento       = models.DateField(blank=True, null=True)
    ativo            = models.BooleanField(default=True, verbose_name='Ativo')
    
    class Meta:
        verbose_name_plural = 'dados'
```

## Editando `pessoas/admin.py`

```python
from django.contrib import admin
from .models import DadosBasicos


class PessoasAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'nome')


admin.site.register(DadosBasicos, PessoasAdmin)
```

## Editando `settings.py`

```python

# incluir o app em INSTALLED APPS
INSTALLED_APPS = [
    ...
    'pessoas.apps.PessoasConfig'
    ...
]
```

## Executando `migrations`

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

## Rodando o projeto

```bash
$ python manage.py runserver
```