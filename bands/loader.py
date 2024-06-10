from bands.models import Banda
from bands.models import Album
from bands.models import Musica
from django.core.exceptions import ObjectDoesNotExist
import json

Banda.objects.all().delete()
Musica.objects.all().delete()
Album.objects.all().delete()

with open('bands/json/bandas.json') as f:
    bandas = json.load(f)

    for banda_info in bandas:
        Banda.objects.create(
            nome=banda_info['nome'],
            nacionalidade=banda_info['nacionalidade'],
            ano_criacao=banda_info['ano_criacao'],
            fotoBanda=banda_info['fotoBanda']
        )

with open('bands/json/discos.json') as f:
    discos = json.load(f)

    for disco_info in discos:
        try:
            banda = Banda.objects.get(nome=disco_info['nome_banda'])
        except ObjectDoesNotExist:
            print(f"Banda não encontrada: {disco_info['nome_banda']}")
            continue

        album = Album.objects.create(
            titulo=disco_info['titulo'],
            ano_lancamento=disco_info['ano_lancamento'],
            data=disco_info['data'],
            capa=disco_info['capa']
        )

        # Adicionando músicas ao álbum
        for musica_info in disco_info['musicas']:
            musica = Musica.objects.create(
                nome=musica_info['nome'],
                duracao=musica_info['duracao'],
                spotify=musica_info['spotify']
            )
            album.musicas.add(musica)

        album.save()
        banda.albuns.add(album)
        banda.save()



# listar o nome das bandas, ordenadas alfabéticamente
print(Banda.objects.values_list('nome',flat=True).order_by('nome'))

# listar o nome dos álbuns de uma banda, ordenados cronológicamente
print(Album.objects.values_list('titulo',flat=True).order_by('data'))

# apresentar todos os álbuns que foram lançados entre dois anos à sua escolha.
print(Album.objects.filter(ano_lancamento__gte=2002,ano_lancamento__lte=2015))

# criar uma playlist de um album, i.e., a lista dos links das músicas.
album = Album.objects.get(titulo='V')
print(album.musicas.values_list('spotify', flat=True))

# listar os albuns com músicas que durem mais de 5 minutos
print(Album.objects.filter(musicas__duracao__gt='5:00').distinct())

# Listar os albuns que começam com a letra 'L'
print( Album.objects.filter(titulo__startswith = 'V').values_list('titulo',flat = True))


