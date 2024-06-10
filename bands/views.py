from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from .forms import BandaForm
from .forms import AlbumForm
from .forms import MusicaForm
from .models import Album
from .models import Musica
from .models import Banda


def index_view(request):

    bandas = Banda.objects.all().order_by('nome')
    return render(request, "bands/index.html",{'bandas': bandas})

def banda_view(request,banda_id):

    banda = Banda.objects.get(id=banda_id)
    albuns = banda.albuns.all()
    user_is_superuser = request.user.is_superuser
    user_is_editor = request.user.groups.filter(name='editores de bandas').exists()

    context = {
        'banda': banda,
        'albuns': albuns,
        'user_is_superuser': user_is_superuser,
        'user_is_editor': user_is_editor,

    }

    return render(request, "bands/banda.html", context)

def album_view(request,album_id):

    album= Album.objects.get(id=album_id)
    bandas = Banda.objects.filter(albuns__id=album_id)
    user_is_superuser = request.user.is_superuser
    user_is_editor = request.user.groups.filter(name='editores de bandas').exists()



    context = {
    'album' : album,
    'bandas': bandas,
    'user_is_superuser': user_is_superuser,
    'user_is_editor': user_is_editor,

    }

    return render(request, "bands/album.html", context)

def musica_view(request,musica_id):

    musica = Musica.objects.get(id=musica_id)
    albuns  = Album.objects.filter(musicas__id=musica_id)
    user_is_superuser = request.user.is_superuser
    user_is_editor = request.user.groups.filter(name='editores de bandas').exists()

    context = {

    'musica': musica,
    'albuns': albuns,
    'user_is_superuser': user_is_superuser,
    'user_is_editor': user_is_editor,
    }

    return render(request, "bands/musica.html",context)


def html5_css_view(request):


    context = {

    }

    return render(request, "bands/html5-css.html",context)















@login_required
def nova_banda_view(request):
    form = BandaForm()

    if form.is_valid():
        form.save()
        return redirect('bands:index')

    context = {'form': form}
    return render(request, 'bands/nova_banda.html', context)

@login_required
def edita_banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)

    if request.POST:
        form = BandaForm(request.POST or None, request.FILES, instance=banda)
        if form.is_valid():
            form.save()
            return redirect('bands:index')
    else:
        form = BandaForm(instance=banda)

    context = {'form': form, 'banda':banda}
    return render(request, 'bands/edita_banda.html', context)

@login_required
def apaga_banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    banda.delete()
    return redirect('bands:index')







@login_required
def novo_album_view(request, banda_id):

    banda= Banda.objects.get(id=banda_id)
    form = AlbumForm(request.POST or None, request.FILES)

    if form.is_valid():
        album = form.save(commit=False)
        album.save()
        banda.albuns.add(album)
        banda.save()
        return redirect('bands:banda', banda_id=banda.id)


    context = {'form': form,'banda': banda}
    return render(request, 'bands/novo_album.html', context)

@login_required
def edita_album_view(request, album_id):
    album = get_object_or_404(Album, id=album_id)

    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('bands:album', album_id=album.id)
    else:
        form = AlbumForm(instance=album)

    context = {'form': form, 'album': album}
    return render(request, 'bands/edita_album.html', context)


@login_required
def apaga_album_view(request, album_id):
    album = Album.objects.get(id=album_id)
    banda = Banda.objects.get(albuns__id=album_id)
    album.delete()
    return redirect('bands:banda',  banda_id=banda.id)







@login_required
def nova_musica_view(request, album_id):

    album = Album.objects.get(id=album_id)

    form = MusicaForm(request.POST or None, request.FILES)

    if form.is_valid():
        musica = form.save(commit=False)
        musica.save()
        album.musicas.add(musica)
        album.save()
        return redirect('bands:musica',musica_id=musica.id)

    context = {'form': form,'album': album}
    return render(request, 'bands/nova_musica.html', context)


@login_required
def edita_musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)

    if request.POST:
        form = MusicaForm(request.POST, request.FILES, instance=musica)
        if form.is_valid():
            form.save()
            return redirect('bands:musica', musica_id=musica.id)
    else:
        form = MusicaForm(instance=musica)

    context = {'form': form, 'musica':musica}
    return render(request, 'bands/edita_musica.html', context)

@login_required
def apaga_musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)
    musica.delete()
    return redirect('bands:bandas')



