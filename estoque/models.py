from django.db import models
from datetime import datetime

# Create your models here.
class Produto(models.Model):
    _id = models.IntegerField()
    descricao = models.CharField(max_length=50)
    quantidade = models.IntegerField()

    def __str__(self):
        return str(self._id) + " - " + self.descricao + " - " + str(self.quantidade)

class Cliente(models.Model):
    _id = models.IntegerField(null=True)
    nome = models.CharField(max_length=50, null=True)
    telefone = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self._id) + " - " + self.nome + " - " + self.telefone

class Vendedor(models.Model):
    _id = models.IntegerField(null=True)
    nome = models.CharField(max_length=50, null=True)
    telefone = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self._id) + " - " + self.nome + " - " + self.telefone

class Venda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.SET_NULL, null=True)
    data = models.DateTimeField(null=True, blank=True, default=datetime.now)

    def __str__(self):
        return str(self.data)

