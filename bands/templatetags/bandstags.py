from django import template
from bands.models import Banda

register = template.Library()

@register.filter
def albuns_ordData(banda_id):
    banda= Banda.objects.get(id=banda_id)
    album = banda.albuns.order_by('-ano_lancamento')

    return album

@register.filter
def mais_albuns(bandas):
    bandas_ordenadas = sorted(bandas, key=lambda banda: banda.albuns.count(), reverse=True)
    return bandas_ordenadas