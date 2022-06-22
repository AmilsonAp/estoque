from django.contrib import admin
from estoque.models import Produto, Venda, Vendedor, Cliente
# Register your models here.

admin.site.register(Produto)
admin.site.register(Venda)
admin.site.register(Vendedor)
admin.site.register(Cliente)


