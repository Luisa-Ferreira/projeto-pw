from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import ComentarioForm
from .forms import ArtigoForm
from .forms import AutorForm
from .models import Artigo
from .models import Comentario
from .models import Autor


from django.contrib.auth.decorators import user_passes_test


def is_superuser(user):
    return user.is_superuser

superuser_required = user_passes_test(is_superuser)



def in_group_editors(user):
    return user.groups.filter(name='editores de bandas').exists()

editors_group_required = user_passes_test(in_group_editors)


def artigos_view(request):
    artigos= Artigo.objects.all()

    return render(request, "artigos/artigos.html", {'artigos':artigos})

def artigo_view(request,artigo_id):
    artigo= Artigo.objects.get(id=artigo_id)

    return render(request, "artigos/artigo.html",{'artigo':artigo})



@login_required
def novo_artigo_view(request):
    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('artigos:artigos')
    else:
        form = ArtigoForm()

    context = {'form': form}
    return render(request, 'artigos/novo_artigo.html', context)

@login_required
def edita_artigo_view(request, artigo_id):
    artigo = Artigo.objects.get(id = artigo_id)

    if request.POST:
        form = ArtigoForm(request.POST or None, request.FILES, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('artigos:artigos')
    else:
        form = ArtigoForm(instance=artigo)

    context = {'form': form, 'artigo':artigo}
    return render(request, 'artigos/edita_artigo.html', context)

@login_required
def apaga_artigo_view(request, artigo_id):
    artigo = Artigo.objects.get(id = artigo_id)
    artigo.delete()
    return redirect('artigos:artigos')







@login_required
def novo_comentario_view(request, artigo_id):

    artigo= Artigo.objects.get(id=artigo_id)
    form = ComentarioForm(request.POST or None, request.FILES)

    if form.is_valid():
        comentario = form.save(commit=False)
        comentario.save()
        artigo.comentarios.add(comentario)
        artigo.save()
        return redirect('artigos:artigo', artigo_id=artigo.id)


    context = {'form': form}
    return render(request, 'artigos/novo_comentario.html', context)

@login_required
@superuser_required
def edita_comentario_view(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)
    artigo= Artigo.objects.get(comentarios=comentario)

    if request.method == 'POST':
        form = ComentarioForm(request.POST, request.FILES, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('artigos:artigo', artigo_id=artigo.id)
    else:
        form = ComentarioForm(instance=comentario)

    context = {'form': form, 'comentario':comentario}
    return render(request, 'artigos/edita_comentario.html', context)


@login_required
@superuser_required
def apaga_comentario_view(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)
    comentario.delete()
    return redirect('artigos:artigos')






@login_required
def novo_autor_view(request):
    if request.method == 'POST':
        form = AutorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('artigos:artigos')
    else:
        form = AutorForm()

    context = {'form': form}
    return render(request, 'artigos/novo_autor.html', context)


@login_required
def edita_autor_view(request, autor_id):

    autor = Autor.objects.get(id=autor_id)

    if request.method == 'POST':
        form = AutorForm(request.POST, request.FILES, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('artigos:artigos')
    else:
        form = AutorForm(instance=autor)

    context = {'form': form, 'autor': autor}
    return render(request, 'artigos/edita_autor.html', context)


@login_required
@superuser_required
def apaga_autor_view(request, autor_id):
    autor = Autor.objects.get(id=autor_id)
    autor.delete()
    return redirect('artigos:artigos')
