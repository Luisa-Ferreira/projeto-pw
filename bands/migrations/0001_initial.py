# Generated by Django 4.0.6 on 2024-05-18 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('ano_lancamento', models.IntegerField()),
                ('data', models.DateField()),
                ('capa', models.ImageField(blank=True, null=True, upload_to='bands/fotos')),
            ],
        ),
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('duracao', models.CharField(max_length=100)),
                ('spotify', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Banda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('nacionalidade', models.CharField(max_length=100, null=True)),
                ('ano_criacao', models.IntegerField()),
                ('fotoBanda', models.ImageField(blank=True, null=True, upload_to='bands')),
                ('albuns', models.ManyToManyField(related_name='bandas', to='bands.album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='musicas',
            field=models.ManyToManyField(related_name='albuns', to='bands.musica'),
        ),
    ]