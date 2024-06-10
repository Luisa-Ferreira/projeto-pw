from django import forms
from .models import Banda
from .models import Album
from .models import Musica
import datetime


class BandaForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = '__all__'

        current_year = datetime.datetime.now().year
        years = [(year, year) for year in range(1950, current_year - 3)]

        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome da Banda'}),
            'nacionalidade': forms.TextInput(attrs={'placeholder': 'Em que país foi criada a banda'}),
            'biografia': forms.Textarea(attrs={'placeholder': 'Insira uma breve biografia de 4-5 linhas.'}),
            'ano_criacao': forms.Select(choices=years, attrs={'placeholder': 'Em que ano foi criada'}),
            'albuns': forms.SelectMultiple(attrs={'placeholder': 'Para selecionar mais de um álbum, mantenha pressionada a tecla Shift'}),
        }
        help_texts = {
            'biografia': 'Insira uma breve biografia de 4-5 linhas.',
            'ano_criacao': 'Clique na opção correta',
            'albuns': 'Para selecionar mais de um álbum, mantenha pressionada a tecla Shift.',
        }


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


        current_year = datetime.datetime.now().year
        years = [(year, year) for year in range(1950, current_year + 1)]

        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Nome do álbum'}),
            'ano_lancamento': forms.Select(choices=years, attrs={'placeholder': 'Ano de lançamento'}),
            'data': forms.DateInput(attrs={
                'type': 'date',
                'placeholder': 'Data de lançamento (dia-mês-ano)'
            }),
        }

        help_texts = {
            'ano_lancamento': 'Selecione o ano de lançamento.',
            'data': 'Insira a data no formato dia-mês-ano.',
            'musicas': 'Para selecionar mais de uma música, mantenha pressionada a tecla Shift.'
        }

    def __init__(self, *args, **kwargs):
        super(AlbumForm, self).__init__(*args, **kwargs)
        current_year = datetime.datetime.now().year
        years = [(year, year) for year in range(1950, current_year + 1)]

        self.fields['ano_lancamento'].widget = forms.Select(choices=years, attrs={'placeholder': 'Ano de lançamento'})


class MusicaForm(forms.ModelForm):
  class Meta:
    model = Musica
    fields = '__all__'

    widgets = {
        'nome': forms.TextInput(attrs={'placeholder': 'Nome da música'}),
        'duracao': forms.TextInput(attrs={'placeholder': 'Duração (minuto:segundo)'}),
        'spotify': forms.URLInput(attrs={'placeholder': 'Link do Spotify'}),
        'letra': forms.Textarea(attrs={'placeholder': 'Letra da música'}),
    }

    help_texts = {
      'nome': 'Insira o nome da música',
      'duracao': 'Insira a durançao no tipo minuto:segundo',
      'spotify': 'tem de ser parecido a https://open.spotify.com/intl-pt/track/',
      'letra': 'Insira a letra da música',
    }