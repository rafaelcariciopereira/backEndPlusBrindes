from rest_framework import serializers
from .models import Product , Category , Fornecedor


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'id' , 'name' , 'description' , 'category'



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("O preço deve ser um valor positivo.")
        return value

    # Validação do campo estoque
    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("O estoque não pode ser negativo.")
        return value

    # Validação para garantir que o fornecedor exista
    def validate_fornecedorPadrao(self, value):
        if not Fornecedor.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Fornecedor não encontrado.")
        return value

    # Validação do relacionamento com a categoria
    def validate_category(self, value):
        if not Category.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Categoria não encontrada.")
        return value
  

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'
