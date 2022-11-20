from django.shortcuts import render, redirect
from app.forms import AlunosForm
from app.models import Alunos
#from django.core.paginator import Paginator

# Create your views here.
def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Alunos.objects.filter(Aluno__icontains=search)
    else:
        data['db'] = Alunos.objects.all()

    #all = Alunos.objects.all()
    #paginator = Paginator(all, 2)
    #pages = request.GET.get('page')
    #data['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = AlunosForm()
    return render(request, 'form.html', data)

def create(request):
    form = AlunosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Alunos.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Alunos.objects.get(pk=pk)
    data['form'] = AlunosForm(instance=data['db'])
    return render(request, 'form.html', data)

def update (request, pk):
    data = {}
    data['db'] = Alunos.objects.get(pk=pk)
    form = AlunosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Alunos.objects.get(pk=pk)
    db.delete()
    return redirect('home')