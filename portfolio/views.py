from django.shortcuts import render
from .models import Luisa
# Create your views here.


def landing_view(request):



    return render(request, "portfolio/landingpage.html")

def mebyme_view(request):

    info= Luisa.objects.get(nome='Luisa')

    return render(request, "portfolio/mebyme.html",{'info':info})

def meuwebsite_view(request):


    return render(request, "portfolio/meuwebsite.html")