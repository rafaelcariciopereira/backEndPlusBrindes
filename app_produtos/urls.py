from django.urls import path
from .views_product import ProdutoListCreateView, ProdutoRetrieveUpdateDestroyView , ProdutoList
from .views_fornecedor import FornecedorListCreateView , FornecedorRetrieveUpdateDestroyView
from .views_category import CategoryListCreateView , CategoryRetrieveUpdateDestroyView


# Rotas:
# 0. '/produtos/' - Metodo: GET (utilizar no Site Comercial)
# 1. '/produtos/criar/' - Métodos: GET (lista todos os produtos) e POST (cria um novo produto).
# 2. '/produtos/<int:pk>/' - Métodos: GET (obtém detalhes de um produto específico), PUT (atualiza os dados de um produto específico) e DELETE (exclui um produto específico).
# 3. '/categorias/' - Métodos: GET (lista todas as categorias) e POST (cria uma nova categoria).
# 4. '/categorias/<int:pk>/' - Métodos: GET (obtém detalhes de uma categoria específica), PUT (atualiza uma categoria existente) e DELETE (exclui uma categoria).
# 5. '/fornecedores/' - Métodos: GET (lista todos os fornecedores) e POST (cria um novo fornecedor).
# 6. '/fornecedores/<int:pk>/' - Métodos: GET (obtém detalhes de um fornecedor específico), PUT (atualiza os dados de um fornecedor) e DELETE (exclui um fornecedor específico).

urlpatterns = [
    
    # Rotas para Product
    path('produtos/', ProdutoList.as_view(), name='produto-list'),
    path('produtos/criar/', ProdutoListCreateView.as_view(), name='produto-list-create'),
    path('produtos/<int:pk>/', ProdutoRetrieveUpdateDestroyView.as_view(), name='produto-detail'),
    
    # Rotas para Category
    path('categorias/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categorias/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),

    # Rotas para Fornecedor
    path('fornecedores/', FornecedorListCreateView.as_view(), name='fornecedor-list-create'),
    path('fornecedores/<int:pk>/', FornecedorRetrieveUpdateDestroyView.as_view(), name='fornecedor-detail'),

]
