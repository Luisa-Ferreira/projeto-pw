from django import template
import re

register = template.Library()

@register.filter
def divisao_objetivos_info(objetivos):

    objetivos_formatados = re.split(r'(\d+\.\s)', objetivos)

    objetivos_paragrafos = ''.join(f'{objetivos_formatados[i]}{objetivos_formatados[i + 1]}<br><br>' for i in range(1, len(objetivos_formatados) - 1, 2))


    return objetivos_paragrafos

@register.filter
def divisao_competencias_info(competencias):

    competencias_formatadas = competencias.split('-')

    competencias_paragrafos = competencias_formatadas[0] + ''.join(f'- {item.strip()}<br><br>' for item in competencias_formatadas[0:])

    competencias= competencias_paragrafos

    return competencias
