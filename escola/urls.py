from django.urls import path
from . import views

urlpatterns = [
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('cursos/<int:id>/', views.detalhe_curso, name='detalhe_curso'),
]
