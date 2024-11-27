from django.urls import path
from .views import OrcamentoCreateView


urlpatterns = [
    path('orcamento/', OrcamentoCreateView.as_view(), name='orcamento-create'),
]