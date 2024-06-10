from django.contrib import admin
from django.utils.html import format_html

from .models import *

admin.site.register(Autor)
admin.site.register(Comentario)
admin.site.register(Artigo)