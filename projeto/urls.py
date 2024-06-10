from django.urls import path
from . import views

app_name = 'projeto'

urlpatterns = [
    path('', views.curso_view, name='curso'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('disciplinas/', views.disciplinas_view, name='disciplinas'),
    path('disciplina/<int:disciplina_id>/', views.disciplina_view, name='disciplina'),
    path('disciplina/<int:disciplina_id>/projeto/', views.projeto_view, name='projeto'),

]