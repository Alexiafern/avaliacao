from django.forms import ModelForm
from app.models import Alunos

# Create the form class.
class AlunosForm(ModelForm):
    class Meta:
        model = Alunos
        fields = ['Aluno', 'Curso', 'Turma']

