from rest_framework import generics
from .models import Orcamento
from .serializers import OrcamentoSerializer

class OrcamentoCreateView(generics.CreateAPIView):
    queryset = Orcamento.objects.all()
    serializer_class = OrcamentoSerializer
