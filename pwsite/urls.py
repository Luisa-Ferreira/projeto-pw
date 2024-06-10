# pwsite/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'pwsite'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('interesses/', views.interesses_view, name='interesses'),
    path('sobre/', views.sobre_view, name='sobre')
]