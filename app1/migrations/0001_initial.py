# Generated by Django 4.0.6 on 2024-03-13 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.IntegerField()),
                ('morada', models.CharField(max_length=100)),
                ('dataDeNascimento', models.DateField()),
            ],
        ),
    ]