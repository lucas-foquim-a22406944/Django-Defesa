from django.contrib import admin
from .models import Categoria, Produto, Endereco, Cliente, Pedido, ItemPedido


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'categoria']
    list_filter = ['categoria']
    search_fields = ['nome']
    ordering = ['preco']


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'data']


admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Endereco)
admin.site.register(ItemPedido)
