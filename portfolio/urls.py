from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.landing_view, name='landing-page'),
    path('mebyme', views.mebyme_view, name='mebyme'),
    path('meuwebsite', views.meuwebsite_view, name='meuwebsite'),
     ]