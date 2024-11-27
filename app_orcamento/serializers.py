from rest_framework import serializers
from .models import Orcamento, OrcamentoProduto
from app_produtos.models import Product

class OrcamentoProdutoSerializer(serializers.ModelSerializer):
    produto_id = serializers.IntegerField(write_only=True)  # Recebe o ID do produto
    quantidade = serializers.IntegerField(default=1)

    class Meta:
        model = OrcamentoProduto
        fields = ['produto_id', 'quantidade']

    def validate_produto_id(self, value):
        """ Valida se o produto existe """
        try:
            Product.objects.get(id=value)
        except Product.DoesNotExist:
            raise serializers.ValidationError(f"Produto com ID {value} não encontrado.")
        return value

class OrcamentoSerializer(serializers.ModelSerializer):
    produtos = OrcamentoProdutoSerializer(many=True)

    class Meta:
        model = Orcamento
        fields = ['nome_cliente', 'email_cliente', 'telefone_cliente', 'endereco_cliente', 'produtos']

    def create(self, validated_data):
        produtos_data = validated_data.pop('produtos')
        
        # Criar o orçamento
        orcamento = Orcamento.objects.create(**validated_data)

        # Criar a relação de produtos
        for produto_data in produtos_data:
            produto = Product.objects.get(id=produto_data['produto_id'])
            OrcamentoProduto.objects.create(
                orcamento=orcamento,
                produto=produto,
                quantidade=produto_data['quantidade']
            )
        
        return orcamento
