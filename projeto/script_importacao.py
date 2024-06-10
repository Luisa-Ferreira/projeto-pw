from projeto.models import Curso
from projeto.models import Disciplina
from projeto.models import Docente
from projeto.models import Area_Cientifica
import json

def importar_curso(ficheiro_json):

    Curso.objects.all().delete()
    Disciplina.objects.all().delete()
    Docente.objects.all().delete()
    Area_Cientifica.objects.all().delete()

    with open(ficheiro_json) as f:

        ficheiro = json.load(f)

        for curso_info in ficheiro['courseDetail'] :

            curso, created = Curso.objects.get_or_create(
                                nome = curso_info['courseName'],
                                apresentacao = curso_info['presentation'],
                                objetivos = curso_info['objectives'],
                                competencias = curso_info['competences'],
                                )

            diretor, created = Docente.objects.get_or_create(
                        nomeDocente = curso_info['directionContact'],
                        email = curso_info['directionEmail']
                        )

            secretaria, created = Docente.objects.get_or_create(
                        nomeDocente = curso_info['courseSecretariatContact'],
                        email = curso_info['courseSecretariatEmail']
                        )

            coordenador, created = Docente.objects.get_or_create(
                        nomeDocente = curso_info['coorCursoContacto'],
                        email = curso_info['coorCursoEmail']
                        )

            curso.docenteCurso.add(diretor)
            curso.docenteCurso.add(secretaria)
            curso.docenteCurso.add(coordenador)


            for disciplina_info in ficheiro['courseFlatPlan'] :

                areaCientifica, created = Area_Cientifica.objects.get_or_create(
                        nomeArea = curso_info['scientificArea']
                        )

                disciplina, created = Disciplina.objects.get_or_create(
                            nomeDisciplina = disciplina_info['curricularUnitName'],
                            ano = disciplina_info['curricularYear'],
                            semestre = disciplina_info['semester'],
                            ects = disciplina_info['ects'],
                            curricularIUnitReadableCode = disciplina_info['curricularIUnitReadableCode'],
                            areaCientifica = areaCientifica,
                            )












