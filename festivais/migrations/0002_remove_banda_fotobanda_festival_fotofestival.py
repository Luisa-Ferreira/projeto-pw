# Generated by Django 4.0.6 on 2024-04-24 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festivais', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banda',
            name='fotoBanda',
        ),
        migrations.AddField(
            model_name='festival',
            name='fotoFestival',
            field=models.ImageField(blank=True, null=True, upload_to='bands'),
        ),
    ]
