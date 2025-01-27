# Generated by Django 4.0.6 on 2024-05-23 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0008_alter_projeto_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='apresentacao',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='curso',
            name='competencias',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='curso',
            name='objetivos',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='semestre',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='conceitosAplicados',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='tecnologiasUsadas',
            field=models.TextField(),
        ),
    ]
