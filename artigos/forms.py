from django import forms
from .models import Artigo
from .models import Comentario
from .models import Autor


class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = '__all__'

        widgets = {
            'autor': forms.Select(attrs={'class': 'form-control'}),
            'data': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Data do artigo'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título do artigo'}),
            'cabecaNoticia': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Cabeça da notícia'}),
            'noticia': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Notícia'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'comentarios': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

        help_texts = {
            'autor': 'Selecione o autor do artigo',
            'data': 'Insira a data do artigo (DD/MM/AAAA)',
            'titulo': 'Insira o título do artigo',
            'cabecaNoticia': 'Apenas 1 a 2 paragrafo',
            'noticia': 'Insira o conteúdo da notícia',
            'foto': 'Faça upload da foto do artigo',
            'comentarios': 'Selecione os comentários relacionados ao artigo. Para selecionar mais do que 1 prima shift',
        }


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'

        widgets = {
            'autor': forms.Select(attrs={'class': 'form-control'}),
            'mensagem': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mensagem do comentário'}),
        }

        help_texts = {
            'autor': 'Selecione o autor do comentário',
            'mensagem': 'Insira a mensagem do comentário',
        }


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

        widgets = {
            'autor': forms.Select(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
        }

        help_texts = {
            'autor': 'Selecione a sua conta',
            'foto': 'Faça upload da foto da sua foto',
            'rating': 'Selecione a sua classificação',
        }