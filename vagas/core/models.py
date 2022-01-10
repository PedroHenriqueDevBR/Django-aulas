from django.db import models

from account.models import Empresa


class Categoria(models.Model):
    nome = models.CharField(max_length=200)


class Vaga(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField(max_length=1500)
    salario = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    data_da_publicacao = models.DateTimeField(auto_now=True)
    encerrada = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='cat_vagas')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='emp_vagas')
