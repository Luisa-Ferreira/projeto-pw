# Generated by Django 4.0.6 on 2024-04-07 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area_Cientifica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeArea', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('apresentacao', models.CharField(max_length=100)),
                ('objetivos', models.CharField(max_length=100)),
                ('competencias', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeDocente', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LinguagemProgramacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linguagem', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=100)),
                ('conceitosAplicados', models.CharField(max_length=100)),
                ('tecnologiasUsadas', models.CharField(max_length=100)),
                ('imagem', models.ImageField(default='default.jpg', upload_to='')),
                ('linkVideo', models.URLField(blank=True)),
                ('linkGithub', models.URLField(blank=True)),
                ('linguagem', models.ManyToManyField(related_name='projetos', to='projeto.linguagemprogramacao')),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeDisciplina', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
                ('semestre', models.CharField(max_length=100)),
                ('ects', models.IntegerField()),
                ('curricularIUnitReadableCode', models.CharField(max_length=100)),
                ('areaCientifica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projeto.area_cientifica')),
                ('cursos', models.ManyToManyField(related_name='disciplinas', to='projeto.curso')),
                ('docentes', models.ManyToManyField(related_name='disciplinas', to='projeto.docente')),
                ('linguagem', models.ManyToManyField(related_name='disciplinas', to='projeto.linguagemprogramacao')),
                ('projeto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='disciplinas', to='projeto.projeto')),
            ],
        ),
    ]
