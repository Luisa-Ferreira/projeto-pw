# Generated by Django 4.0.6 on 2024-04-20 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0003_alter_curso_apresentacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='docenteCurso',
            field=models.ManyToManyField(related_name='curso', to='projeto.docente'),
        ),
    ]
