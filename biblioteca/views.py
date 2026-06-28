from django.shortcuts import render, get_object_or_404
from .models import Livro, Autor


def lista_livros(request):
    livros = Livro.objects.select_related('autor').all()
    return render(request, 'biblioteca/livros.html', {'livros': livros})


def lista_autores(request):
    autores = Autor.objects.all().order_by('nome')
    return render(request, 'biblioteca/autores.html', {'autores': autores})


def detalhe_autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    livros = autor.livro_set.all()
    return render(request, 'biblioteca/autor.html', {'autor': autor, 'livros': livros})
