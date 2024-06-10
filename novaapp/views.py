from django.shortcuts import render, get_object_or_404
import random
from .models import Verdade
from .models import Consequencia

def index_view(request):
    return render(request, "novaapp/index.html")

def consequencia_view(request):

    min_id = Consequencia.objects.order_by('id').first().id
    max_id = Consequencia.objects.order_by('-id').first().id


    random_id = random.randint(min_id, max_id)


    consequencia = get_object_or_404(Consequencia, id=random_id)

    context = {
        'consequencia': consequencia,
        'id_conseq':random_id

        }

    return render(request, "novaapp/consequencia.html", context)

def verdade_view(request):
    min_id = Verdade.objects.order_by('id').first().id
    max_id = Verdade.objects.order_by('-id').first().id


    random_id = random.randint(min_id, max_id)

    verdade = get_object_or_404(Verdade, id=random_id)

    context = {
        'verdade': verdade,
        'id_verd':random_id

        }

    return render(request, "novaapp/verdade.html",context)
