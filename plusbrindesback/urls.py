from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app_produtos.urls')),
    path('orc/', include('app_orcamento.urls'))
]
