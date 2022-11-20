from django.db import models

# Create your models here.
class Alunos(models.Model):
    Aluno = models.CharField(max_length=150)
    Curso = models.CharField(max_length=100)
    Turma = models.IntegerField()