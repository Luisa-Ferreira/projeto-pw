from django.urls import path
from . import views

app_name = 'artigos'

urlpatterns = [
    path('artigos/', views.artigos_view, name='artigos'),
    path('artigo/<int:artigo_id>/', views.artigo_view, name='artigo'),

    path('artigo/novo', views.novo_artigo_view, name="novo_artigo"),
    path('artigo/<int:artigo_id>/edita', views.edita_artigo_view,name="edita_artigo"),
    path('artigo/<int:artigo_id>/apaga', views.apaga_artigo_view,name="apaga_artigo"),

    path('comentario/<int:artigo_id>/novo', views.novo_comentario_view,name="novo_comentario"),
    path('comentario/<int:comentario_id>/edita', views.edita_comentario_view,name="edita_comentario"),
    path('comentario/<int:comentario_id>/apaga', views.apaga_comentario_view,name="apaga_comentario"),

    path('autor/novo/', views.novo_autor_view,name="novo_autor"),
    path('autor/<int:autor_id>/edita', views.edita_autor_view,name="edita_autor"),
    path('autor/<int:autor_id>/apaga', views.apaga_autor_view,name="apaga_autor"),

]