from django.urls import path
from . import views

app_name = 'noobsite'

urlpatterns = [
    path('index/', views.index_view),
    path('intro/', views.intro),
    path('hello/<str:nome>/', views.Hello),
]