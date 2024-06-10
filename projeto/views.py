from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Disciplina
from .models import Curso
from .models import Projeto


def curso_view(request):

    curso = Curso.objects.get(nome='Engenharia Informática')


    return render(request, "projeto/curso.html",{'curso':curso})

def disciplinas_view(request):

    disciplinas= Disciplina.objects.all().order_by('nomeDisciplina')

    return render(request, "projeto/disciplinas.html",{'disciplinas':disciplinas})

def disciplina_view(request,disciplina_id):

    context = {
    'disciplina':Disciplina.objects.get(id=disciplina_id),
    }

    return render(request, "projeto/disciplina.html",context)


def projetos_view(request):
    disciplinas= Disciplina.objects.all()
    return render(request, "projeto/projetos.html", {'disciplinas': disciplinas})

def projeto_view(request,disciplina_id):
    disciplina= Disciplina.objects.get(id=disciplina_id)

    context = {
    'disciplina': disciplina,
    'projeto': disciplina.projeto if disciplina.projeto else None
    }

    return render(request, "projeto/projeto.html", context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('projeto:curso')