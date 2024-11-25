from rest_framework import generics
from .models import Fornecedor
from .serializers import FornecedorSerializer



class FornecedorListCreateView(generics.ListCreateAPIView):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

class FornecedorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer
