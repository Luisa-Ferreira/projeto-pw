from django.urls import path
from . import views

app_name = 'festivais'

urlpatterns = [
    path('localizacao/', views.localizacao_view, name='localizacao'),
    path('localizacao/<int:festival_id>/', views.festival_view, name='festival'),
]