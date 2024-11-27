from django.contrib import admin
from .models import Product , Fornecedor , Category
# Register your models here.

admin.site.register(Product)
admin.site.register(Fornecedor)
admin.site.register(Category)