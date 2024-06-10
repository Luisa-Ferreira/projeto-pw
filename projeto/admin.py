from django.contrib import admin
from django.utils.html import format_html
from .models import Curso
from .models import Area_Cientifica
from .models import Disciplina
from .models import Docente
from .models import Projeto
from .models import LinguagemProgramacao

admin.site.register(Curso)
admin.site.register(Area_Cientifica)
admin.site.register(Disciplina)
admin.site.register(Docente)
admin.site.register(Projeto)
admin.site.register(LinguagemProgramacao)