# pwsite/views.py

from django.shortcuts import render
import datetime

def index_view(request):
    current_date = datetime.datetime.now()
    return render(request, "pwsite/index.html",{'current_date': current_date})

def interesses_view(request):
    return render(request, "pwsite/interesses.html")

def sobre_view(request):
    return render(request, "pwsite/sobre.html")