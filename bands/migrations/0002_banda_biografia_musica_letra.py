# Generated by Django 4.0.6 on 2024-06-01 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banda',
            name='biografia',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='musica',
            name='letra',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
