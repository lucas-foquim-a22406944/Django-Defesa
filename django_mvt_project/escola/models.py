from django.db import models


class Professor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Curso(models.Model):
    idioma = models.CharField(max_length=100)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.idioma


class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    cursos = models.ManyToManyField(Curso, blank=True)

    def __str__(self):
        return self.nome
