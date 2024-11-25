from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Categoria")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Fornecedor(models.Model):
    name = models.CharField(max_length=200)
    codFornecedor = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    fornecedorPadrao = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, related_name="fornecedor")
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name
