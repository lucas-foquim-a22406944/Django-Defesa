# Django MVT Project

Projeto Django com 3 aplicações desenvolvidas como exercícios MVT.

## Aplicações

- **biblioteca** — Autores, Livros e Géneros (ForeignKey + ManyToMany)
- **escola** — Professores, Cursos e Estudantes (ForeignKey + ManyToMany)
- **loja** — Categorias, Produtos, Clientes, Pedidos e Itens (ForeignKey + OneToOne)

## Instalação

```bash
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## URLs disponíveis

| URL | Descrição |
|-----|-----------|
| `/admin/` | Interface admin |
| `/biblioteca/livros/` | Lista de livros |
| `/biblioteca/autores/` | Lista de autores |
| `/biblioteca/autores/<id>/` | Detalhe de autor |
| `/escola/cursos/` | Lista de cursos |
| `/escola/cursos/<id>/` | Detalhe de curso |
| `/loja/produtos/` | Produtos por categoria |
| `/loja/clientes/<id>/pedidos/` | Pedidos de um cliente |
