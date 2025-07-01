from django.db import models

# Create your models here.
class ideiasModel(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=255)
    data_criacao = models.DateTimeField(auto_now_add=True)
    