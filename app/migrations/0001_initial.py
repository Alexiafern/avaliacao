# Generated by Django 4.1.3 on 2022-11-19 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alunos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Aluno', models.CharField(max_length=150)),
                ('Curso', models.CharField(max_length=100)),
                ('Turma', models.IntegerField()),
            ],
        ),
    ]