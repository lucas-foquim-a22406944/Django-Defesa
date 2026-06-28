from django.contrib import admin
from .models import Autor, Genero, Livro


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor']
    search_fields = ['titulo']
    list_filter = ['generos']
    filter_horizontal = ['generos']


admin.site.register(Genero)
