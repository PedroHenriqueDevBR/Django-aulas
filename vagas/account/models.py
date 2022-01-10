from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Localidade(models.Model):
    nome = models.CharField(max_length=250)


class Empresa(models.Model):
    contato = models.CharField(max_length=20)
    localidade = models.ForeignKey(Localidade, on_delete=models.CASCADE, related_name='loc_empresas')
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='empresa')