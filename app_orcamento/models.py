from django.db import models
from app_produtos.models import Product

# Create your models here.

class Orcamento(models.Model):
    nome_cliente = models.CharField(max_length=255) 
    email_cliente = models.EmailField()  
    telefone_cliente = models.CharField(max_length=20, blank=True, null=True) 
    endereco_cliente = models.TextField(blank=True, null=True)
    produtos = models.ManyToManyField(Product, through='OrcamentoProduto')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Orçamento #{self.id} - {self.nome_cliente}"


class OrcamentoProduto(models.Model):
    orcamento = models.ForeignKey(Orcamento, on_delete=models.CASCADE)
    produto = models.ForeignKey(Product, on_delete=models.CASCADE)  
    quantidade = models.PositiveIntegerField(default=1)  

    def __str__(self):
        return f"{self.quantidade}x {self.produto.name} (Orçamento: {self.orcamento.nome_cliente})"
