from django.shortcuts import render
from .models import Festival
from .models import Banda
from .models import Localizacao

def localizacao_view(request):

    context = {
    'localizacao' : Localizacao.objects.all(),
    'festivais' : Festival.objects.all(),
    }

    return render(request, "festivais/localizacao.html",context)

def festival_view(request,festival_id):
    festival= Festival.objects.get(id=festival_id)

    context = {
    'festival': festival,
    'localizacao': Localizacao.objects.get(festivais=festival),
    }
    return render(request, "festivais/festival.html",context)
