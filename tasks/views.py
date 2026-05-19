from django.shortcuts import render, redirect
from .models import Task
from .forms import CadastroForm, TarefaForm

def dashboard(request):
    tarefas = Task.objects.all()
    return render(request, 'tasks/dashboard.html', {'tarefas': tarefas})

def login_view(request):
    return render(request, 'tasks/login.html')

def cadastro(request):
    form = CadastroForm()
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    return render(request, 'tasks/cadastro.html', {'form': form})

def criar_tarefa(request):
    form = TarefaForm()
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.usuario = request.user
            tarefa.save()
            return redirect('dashboard')
    return render(request, 'tasks/criar_tarefa.html', {'form': form})

def editar_tarefa(request, id):
    return render(request, 'tasks/editar_tarefa.html')

def detalhe_tarefa(request, id):
    return render(request, 'tasks/detalhe_tarefa.html')