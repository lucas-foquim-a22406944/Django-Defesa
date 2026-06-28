from django.contrib import admin
from .models import Professor, Curso, Estudante


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['idioma', 'professor']
    search_fields = ['idioma']


@admin.register(Estudante)
class EstudanteAdmin(admin.ModelAdmin):
    list_display = ['nome']
    filter_horizontal = ['cursos']


admin.site.register(Professor)
