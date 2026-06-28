from django.shortcuts import render, get_object_or_404
from .models import Curso, Estudante


def lista_cursos(request):
    cursos = Curso.objects.select_related('professor').all()
    return render(request, 'escola/cursos.html', {'cursos': cursos})


def detalhe_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    estudantes = curso.estudante_set.all()
    return render(request, 'escola/curso.html', {'curso': curso, 'estudantes': estudantes})
