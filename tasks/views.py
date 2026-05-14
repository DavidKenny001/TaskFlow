from django.shortcuts import render
from .models import Task

def dashboard(request):
    tarefas = Task.objects.all()
    return render(request, 'tasks/dashboard.html', {'tarefas': tarefas})

def login_view(request):
    return render(request, 'tasks/login.html')

def cadastro(request):
    return render(request, 'tasks/cadastro.html')

def criar_tarefa(request):
    return render(request, 'tasks/criar_tarefa.html')

def editar_tarefa(request, id):
    return render(request, 'tasks/editar_tarefa.html')

def detalhe_tarefa(request, id):
    return render(request, 'tasks/detalhe_tarefa.html')