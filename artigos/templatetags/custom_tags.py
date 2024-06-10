from django import template

register = template.Library()

@register.filter
def comentarios_orderRate(comentarios):

    comentarios_rate= sorted(comentarios, key=lambda comentario: comentario.autor.rating, reverse=True)

    return comentarios_rate