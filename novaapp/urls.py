from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'novaapp'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('consequencia/', views.consequencia_view, name='consequencia'),
    path('verdade/', views.verdade_view, name='verdade'),
]