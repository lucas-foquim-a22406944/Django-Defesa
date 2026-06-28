from django.shortcuts import render, get_object_or_404
from .models import Categoria, Cliente


def lista_produtos(request):
    categorias = Categoria.objects.prefetch_related('produto_set').all()
    return render(request, 'loja/produtos.html', {'categorias': categorias})


def pedidos_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    pedidos = cliente.pedido_set.prefetch_related('itempedido_set__produto').all()
    return render(request, 'loja/pedidos.html', {'cliente': cliente, 'pedidos': pedidos})
