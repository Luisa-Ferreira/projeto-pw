from django.urls import path
from . import views

app_name = 'meteo'

urlpatterns = [
    path('lisboa/', views.lisboa_view, name='lisboa'),
    path('', views.cidades_view, name='cidades'),
    path('cidade/<int:cidade_id>/<int:dia_id>', views.cidade_view, name='cidade'),
]