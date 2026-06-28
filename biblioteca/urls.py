from django.urls import path
from . import views

urlpatterns = [
    path('livros/', views.lista_livros, name='lista_livros'),
    path('autores/', views.lista_autores, name='lista_autores'),
    path('autores/<int:id>/', views.detalhe_autor, name='detalhe_autor'),
]
