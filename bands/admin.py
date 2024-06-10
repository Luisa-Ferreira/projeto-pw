from django.contrib import admin
from django.utils.html import format_html

from .models import *

admin.site.register(Musica)
admin.site.register(Album)
admin.site.register(Banda)